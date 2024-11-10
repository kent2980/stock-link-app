import re
from collections import namedtuple
from typing import List

import app.schema as sc
from app.api.deps import SessionDep
from app.models import IxHeadTitle, IxQualitative
from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlmodel import select
from treelib import Node, Tree

router = APIRouter()


@router.post("/qualitative/", response_model=sc.ix_qualitative.IxQualitativePublic)
def create_ix_qualitative_item(
    *, session: SessionDep, item_in: sc.ix_qualitative.IxQualitativeCreate
) -> sc.ix_qualitative.IxQualitativePublic:
    """
    提携情報をIxQualitativeテーブルに登録する

    Raises:
        HTTPException: アイテムが既に存在する場合

    Returns:
        sc.ix_qualitative.IxQualitativePublic: 登録したアイテム
    """

    statement = select(IxQualitative).where(IxQualitative.id == item_in.id)
    result = session.exec(statement).first()

    if len(result) > 0:
        raise HTTPException(status_code=400, detail="Item already exists")

    item = IxQualitative.model_validate(item_in)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.post(
    "/qualitative/list/", response_model=sc.ix_qualitative.IxQualitativePublics
)
def create_ix_qualitative_items_exists(
    *, session: SessionDep, items_in: sc.ix_qualitative.IxQualitativeCreates
) -> sc.ix_qualitative.IxQualitativePublics:
    """
    提携情報をIxQualitativeテーブルに登録する

    Raises:
        HTTPException: アイテムが既に存在する場合

    Returns:
        sc.ix_qualitative.IxQualitativePublics: 登録したアイテム
    """

    new_items = []
    for item in items_in.data:
        item = IxQualitative.model_validate(item)
        session.add(item)
        try:
            session.commit()
            session.refresh(item)
            new_items.append(item)
        except IntegrityError:
            session.rollback()
    return sc.ix_qualitative.IxQualitativePublics(count=len(new_items), data=new_items)


@router.post(
    "/qualitative/list/update/", response_model=sc.ix_qualitative.IxQualitativePublics
)
def update_ix_qualitative_items(
    *, session: SessionDep, items_in: sc.ix_qualitative.IxQualitativeCreates
) -> sc.ix_qualitative.IxQualitativePublics:
    """
    提携情報をIxQualitativeテーブルに登録する

    Raises:
        HTTPException: アイテムが存在しない場合

    Returns:
        sc.ix_qualitative.IxQualitativePublics: 登録したアイテム
    """

    try:
        first_item = items_in.data[0]
        statement = select(IxQualitative).where(
            IxQualitative.head_item_key == first_item.head_item_key
        )
        result = session.exec(statement).first()

        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
    except IndexError:
        return sc.ix_qualitative.IxQualitativePublics(count=0, data=[])

    new_items = []
    for item in items_in.data:
        statement = select(IxQualitative).where(IxQualitative.id == item.id)
        result = session.exec(statement).first()

        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")

        item = IxQualitative.model_validate(item)
        session.add(item)
        new_items.append(item)

    session.commit()

    return sc.ix_qualitative.IxQualitativePublics(count=len(new_items), data=new_items)


@router.get("/qualitative/is/{head_item_key}/", response_model=bool)
def is_ix_qualitative_item_exists(*, session: SessionDep, head_item_key: str) -> bool:
    """
    提携情報がIxQualitativeテーブルに存在するか確認する

    Returns:
        bool: アイテムが存在する場合はTrue
    """

    return False


@router.get("/qualitative/", response_model=sc.ix_qualitative.QualitativeInfoHeader)
def read_ix_qualitative_item(
    *,
    session: SessionDep,
    head_item_key: str = Query(..., min_length=36, max_length=36),
) -> sc.ix_qualitative.QualitativeInfoHeader:
    """
    提携情報をIxQualitativeテーブルから取得する

    Raises:
        HTTPException: アイテムが存在しない場合

    Returns:
        sc.ix_qualitative.IxQualitativePublic: 取得したアイテム
    """

    statement = (
        select(IxQualitative)
        .where(IxQualitative.head_item_key == head_item_key)
        .order_by(IxQualitative.id)
    )
    result = session.exec(statement).all()

    if result is None or len(result) == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    tree = Tree()
    if not tree.contains("root"):
        tree.create_node("root", "root")

    for item in result:
        currentId = item.currentId
        parentId = item.parentId
        if parentId is None:
            parentId = "root"
        tree.create_node(currentId, currentId, parent=parentId, data=item)

    result = extract_tree_content(tree)

    header = sc.ix_qualitative.QualitativeInfoHeader()
    header.qualitative_info.operating_result_info = result.operating_text
    header.qualitative_info.segment_info_key = result.segment_headers
    header.qualitative_info.segment_info = result.segment_info
    header.qualitative_info.explanation_of_financial_position = (
        result.explanation_of_financial_position
    )
    header.qualitative_info.forecast_info = result.forecast_info
    header.qualitative_info.segment_photo_url = result.segment_photo_url

    return header


def extract_tree_content(tree: Tree):

    result = namedtuple(
        "Result",
        [
            "operating_text",
            "segment_headers",
            "segment_info",
            "explanation_of_financial_position",
            "forecast_info",
            "segment_photo_url",
        ],
    )

    operating_text = ""
    segment_headers = []
    segment_info = {}
    segment_photo_url = {}
    explanation_of_financial_position = ""
    forecast_info = ""
    for node in tree.children("root"):
        node: Node
        if node.is_root():
            continue
        if node.data is None:
            continue
        if node.data.order == 0:  # 当四半期決算に関する定性的情報
            count = -1
            for child in tree.children(node.identifier):
                if "(1)" in child.data.content:
                    count += 1
            for child in tree.children(node.identifier):
                child: Node
                if child.data.order == count:  # 経営成績に関する説明
                    for grandchild in tree.children(child.identifier):
                        grandchild: Node
                        if grandchild.data.type == "content":  # 経営成績に関する説明
                            operating_text += f"{grandchild.data.content}\n"
                        if grandchild.data.type == "heading":  # セグメント情報
                            segment = grandchild.data.content
                            segment = re.sub(r"[①-⑳,\(\),\<\>,\[\]]", "", segment)
                            segment = re.sub(r"^[a-zA-Z]\.|^[ア-ン]\.", "", segment)
                            segment_headers.append(segment)
                            segment_photo_url[segment] = grandchild.data.photo_url
                            for greatGrandChild in tree.children(grandchild.identifier):
                                greatGrandChild: Node
                                if greatGrandChild.data.type == "content":
                                    segment_info[segment] = (
                                        segment_info.get(segment, "")
                                        + f"{greatGrandChild.data.content}\n"
                                    )
                elif child.data.order == count + 1:  # 財政状態に関する説明
                    for grandchild in tree.children(child.identifier):
                        grandchild: Node
                        for greatGrandChild in tree.children(grandchild.identifier):
                            greatGrandChild: Node
                            if greatGrandChild.data.type == "content":
                                explanation_of_financial_position += (
                                    f"{greatGrandChild.data.content}\n"
                                )
                elif child.data.order == count + 2:  # 将来予測に関する説明
                    for grandchild in tree.children(child.identifier):
                        grandchild: Node
                        if grandchild.data.type == "content":
                            forecast_info += f"{grandchild.data.content}\n"

    return result(
        operating_text,
        segment_headers,
        segment_info,
        explanation_of_financial_position,
        forecast_info,
        segment_photo_url,
    )


@router.delete("/qualitative/delete/", response_model=bool)
def delete_ix_qualitative_item(
    *, session: SessionDep, head_item_key: str = Query(...)
) -> bool:
    """
    提携情報をIxQualitativeテーブルから削除する

    Raises:
        HTTPException: アイテムが存在しない場合

    Returns:
        bool: 削除した場合はTrue
    """

    statement = select(IxQualitative).where(
        IxQualitative.head_item_key == head_item_key
    )
    result = session.exec(statement).all()

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    for item in result:
        session.delete(item)

    session.commit()

    return True


@router.get("/content/search/", response_model=List[str])
def search_content(*, session: SessionDep, keyword: str = Query(...)) -> List[str]:
    """
    定性情報から指定したキーワードを検索し、該当する証券コードを取得します

    Properties:
        - session: SessionDep - セッション
        - keyword: str      - 検索キーワード

    Returns:
        List[str]: 証券コードのリスト
    """

    statement = (
        select(IxHeadTitle.securities_code)
        .distinct()
        .join(IxQualitative, IxHeadTitle.item_key == IxQualitative.head_item_key)
        .where(IxQualitative.content.ilike(f"%{keyword}%"))
    )
    result = session.exec(statement).all()

    return result
