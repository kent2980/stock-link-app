from typing import Any, List, Optional, TypeVar

import app.schema as sc
from app.core.security import get_password_hash, verify_password
from app.models import (
    Item,
    ItemCreate,
    IxArcsBase,
    IxCalculationArc,
    IxCalculationLoc,
    IxDefinitionArc,
    IxDefinitionLoc,
    IxFilePath,
    IxHeadTitle,
    IxLabelArc,
    IxLabelLoc,
    IxLabelValue,
    IxLocsBase,
    IxNonFraction,
    IxNonNumeric,
    IxSourceFile,
    ScLinkBaseRef,
    User,
    UserCreate,
    UserUpdate,
)
from sqlalchemy.orm import aliased
from sqlmodel import Session, and_, not_, select


def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def update_user(*, session: Session, db_user: User, user_in: UserUpdate) -> Any:
    user_data = user_in.model_dump(exclude_unset=True)
    extra_data = {}
    if "password" in user_data:
        password = user_data["password"]
        hashed_password = get_password_hash(password)
        extra_data["hashed_password"] = hashed_password
    db_user.sqlmodel_update(user_data, update=extra_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user_by_email(*, session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    session_user = session.exec(statement).first()
    return session_user


def authenticate(*, session: Session, email: str, password: str) -> User | None:
    db_user = get_user_by_email(session=session, email=email)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user


def create_item(*, session: Session, item_in: ItemCreate, owner_id: int) -> Item:
    db_item = Item.model_validate(item_in, update={"owner_id": owner_id})
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def create_ix_head_title(
    *, session: Session, item_in: sc.ix_head.IxHeadTitleCreate
) -> IxHeadTitle:
    db_item = IxHeadTitle.model_validate(item_in)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def create_ix_non_numeric(
    *, session: Session, item_in: sc.ix_non_numeric.IxNonNumericCreate
) -> IxNonNumeric:
    db_item = IxNonNumeric.model_validate(item_in)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def create_ix_non_fraction(
    *, session: Session, item_in: sc.ix_non_fraction.IxNonFractionCreate
) -> IxNonFraction:
    db_item = IxNonFraction.model_validate(item_in)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def create_ix_calculation_loc(
    *, session: Session, item_in: sc.ix_cal.IxCalculationLocCreate
) -> IxCalculationLoc:
    db_item = IxCalculationLoc.model_validate(item_in)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def create_ix_calculation_arc(
    *, session: Session, item_in: sc.ix_cal.IxCalculationArcCreate
) -> IxCalculationArc:
    db_item = IxCalculationArc.model_validate(item_in)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def create_ix_source_file(
    *, session: Session, item_in: sc.ix_source.IxSourceFileCreate
) -> IxSourceFile:
    db_item = IxSourceFile.model_validate(item_in)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def create_ix_file_path(
    *, session: Session, item_in: sc.ix_file_path.IxFilePathCreate
) -> IxFilePath:
    db_item = IxFilePath.model_validate(item_in)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


T1 = TypeVar("T1", bound=IxArcsBase)
T2 = TypeVar("T2", bound=IxLocsBase)


def read_menu_label(session: Session, head_item_key: str, type: str):
    abr = aliased(ScLinkBaseRef)
    ida = aliased(IxDefinitionArc)
    idl = aliased(IxDefinitionLoc)
    ill = aliased(IxLabelLoc)
    ila = aliased(IxLabelArc)
    ilv = aliased(IxLabelValue)

    arcrole = [
        "http://xbrl.org/int/dim/arcrole/all",
    ]
    labelRole = {
        "sm": "http://www.xbrl.org/2003/role/label",
        "fr": "http://www.xbrl.org/2003/role/verboseLabel",
    }
    # head_item_keyからサブタイトルを抽出
    statement = (
        select(abr.head_item_key, ida.xlink_from, idl.xlink_href)
        .join(ida, abr.href_source_file_id == ida.source_file_id)
        .join(
            idl,
            and_(
                abr.href_source_file_id == idl.source_file_id,
                ida.xlink_from == idl.xlink_label,
            ),
        )
        .where(
            abr.head_item_key == head_item_key,
            abr.xbrl_type == type,
            ida.xlink_arcrole.in_(arcrole),
        )
        .order_by(ida.id.asc())
    )
    subquery = statement.subquery()
    statement2 = (
        select(subquery.c.xlink_href, ilv.label)
        .join(abr, subquery.c.head_item_key == abr.head_item_key)
        .join(
            ill,
            and_(
                abr.href_source_file_id == ill.source_file_id,
                subquery.c.xlink_href == ill.xlink_href,
            ),
        )
        .join(
            ila,
            and_(
                ill.source_file_id == ila.source_file_id,
                ill.xlink_label == ila.xlink_from,
            ),
        )
        .join(
            ilv,
            and_(
                ila.source_file_id == ilv.source_file_id,
                ila.xlink_to == ilv.xlink_label,
            ),
        )
        .where(ilv.xlink_role == labelRole[type])
    )
    result = session.exec(statement2)
    items = result.all()

    return items


def read_menu_items(
    session: Session, head_item_key: str, xbrl_type: str
) -> sc.ix_global.MenuItems:
    """メニューアイテムを取得する"""

    # region モデルのエイリアス
    idl = aliased(IxDefinitionLoc)
    # endregion

    # region クエリの作成
    # サブクエリ1
    subquery1 = (
        select(
            IxDefinitionArc.id,
            IxDefinitionArc.xlink_to,
            IxDefinitionArc.xlink_from,
            IxDefinitionArc.attr_value,
            IxDefinitionArc.source_file_id,
            IxDefinitionArc.xlink_arcrole,
            IxDefinitionLoc.xlink_href,
            IxDefinitionLoc.xlink_href.label("from_href"),
            idl.xlink_href.label("to_href"),
            IxDefinitionArc.xlink_order,
        )
        .join(
            IxDefinitionLoc,
            (IxDefinitionArc.head_item_key == IxDefinitionLoc.head_item_key)
            & (IxDefinitionArc.xlink_from == IxDefinitionLoc.xlink_label)
            & (IxDefinitionArc.attr_value == IxDefinitionLoc.attr_value),
            isouter=True,
        )
        .join(
            idl,
            (IxDefinitionArc.head_item_key == idl.head_item_key)
            & (IxDefinitionArc.xlink_to == idl.xlink_label)
            & (IxDefinitionArc.attr_value == idl.attr_value),
            isouter=True,
        )
        .join(
            ScLinkBaseRef,
            (IxDefinitionArc.source_file_id == ScLinkBaseRef.href_source_file_id)
            & (ScLinkBaseRef.xbrl_type == xbrl_type),
        )
        .where(
            IxDefinitionArc.head_item_key == head_item_key,
            IxDefinitionArc.xlink_arcrole
            != "http://www.xbrl.org/2003/arcrole/general-special",
        )
        .subquery()
    )

    # サブクエリ2
    subquery2 = (
        select(
            IxDefinitionArc.id.label("from_id"),
            IxDefinitionLoc.xlink_href,
            IxDefinitionArc.attr_value,
            IxDefinitionArc.source_file_id,
        )
        .join(
            IxDefinitionLoc,
            (IxDefinitionArc.source_file_id == IxDefinitionLoc.source_file_id)
            & (IxDefinitionArc.xlink_to == IxDefinitionLoc.xlink_label)
            & (IxDefinitionArc.attr_value == IxDefinitionLoc.attr_value),
            isouter=True,
        )
        .where(
            IxDefinitionArc.head_item_key == head_item_key,
            IxDefinitionArc.xlink_arcrole
            != "http://xbrl.org/int/dim/arcrole/dimension-default",
        )
        .subquery()
    )

    # メインクエリ
    query = (
        select(
            subquery1.c.id,
            subquery2.c.from_id,
            subquery1.c.xlink_to,
            subquery1.c.xlink_from,
            subquery1.c.attr_value,
            subquery1.c.xlink_arcrole,
            subquery1.c.to_href,
            subquery1.c.from_href,
            subquery1.c.xlink_order,
        )
        .outerjoin(
            subquery2,
            (subquery1.c.source_file_id == subquery2.c.source_file_id)
            & (subquery1.c.xlink_href == subquery2.c.xlink_href)
            & (subquery1.c.attr_value == subquery2.c.attr_value),
        )
        .order_by(subquery1.c.id.asc())
    )
    # endregion

    # region クエリの実行
    result = session.exec(query).all()
    # endregion

    # region 結果をオブジェクト化して返す
    return sc.ix_global.MenuItems(count=len(result), data=result)
    # endregion


def read_finance_item(
    session: Session, head_item_key: str, xbrl_type: str
) -> Optional[sc.ix_global.IxViewFinances]:
    """財務情報を取得"""

    data: List[sc.ix_global.IxViewFinance] = []

    # region 非分数データの取得
    infQuery = select(IxNonFraction).where(
        IxNonFraction.head_item_key == head_item_key,
        IxNonFraction.xbrl_type == xbrl_type,
        IxNonFraction.xsi_nil == False,
    )
    inf_result = session.exec(infQuery).all()

    for item in inf_result:
        data.append(
            sc.ix_global.IxViewFinance(
                name=item.name,
                is_numeric=True,
                type=item.unit_ref,
                context=item.context,
                numeric=item.numeric,
                value=item.display_numeric,
                display_scale=item.display_scale,
            )
        )
    # endregion

    # region 非数値データの取得
    innQuery = select(IxNonNumeric).where(
        IxNonNumeric.head_item_key == head_item_key,
        IxNonNumeric.xbrl_type == xbrl_type,
        IxNonNumeric.xsi_nil == False,
        not_(
            and_(
                IxNonNumeric.value == "false", IxNonNumeric.name.like("%StockExchange%")
            )
        ),
    )
    inn_result = session.exec(innQuery).all()

    for item in inn_result:
        data.append(
            sc.ix_global.IxViewFinance(
                name=item.name,
                type=item.format,
                context=item.context,
                value=item.value,
            )
        )
    # endregion

    return sc.ix_global.IxViewFinances(count=len(data), data=data)
    # endregion


def read_finance_item_label(
    session: Session,
    head_item_key: str,
    xbrl_type: str,
    name: str,
) -> str:
    """財務情報の日本語ラベルを取得"""

    # region クエリの作成
    labelQuery = (
        select(IxLabelValue.label)
        .join(
            IxLabelArc,
            (IxLabelValue.source_file_id == IxLabelArc.source_file_id)
            & (IxLabelValue.xlink_label == IxLabelArc.xlink_to)
            & (IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/label"),
        )
        .join(
            IxLabelLoc,
            (IxLabelValue.source_file_id == IxLabelLoc.source_file_id)
            & (IxLabelArc.xlink_from == IxLabelLoc.xlink_label),
        )
        .join(
            ScLinkBaseRef,
            (ScLinkBaseRef.head_item_key == head_item_key)
            & (ScLinkBaseRef.xbrl_type == xbrl_type)
            & (IxLabelValue.source_file_id == ScLinkBaseRef.href_source_file_id),
        )
        .where(IxLabelLoc.xlink_href == name)
    )
    # endregion

    # region クエリの実行
    label = session.exec(labelQuery).first()
    # endregion

    # region 結果を返す
    if label is None:
        return ""

    return str(label)
    # endregion


def read_finance_item_labels(
    session: Session,
    head_item_key: str,
    xbrl_type: str,
    names: List[str],
) -> sc.ix_global.TreeLabels:
    """財務情報の日本語ラベルを取得"""

    # region クエリの作成
    labelQuery = (
        select(IxLabelValue.label, IxLabelLoc.xlink_href.label("tag"))
        .join(
            IxLabelArc,
            (IxLabelValue.source_file_id == IxLabelArc.source_file_id)
            & (IxLabelValue.xlink_label == IxLabelArc.xlink_to)
            & (IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/label"),
        )
        .join(
            IxLabelLoc,
            (IxLabelValue.source_file_id == IxLabelLoc.source_file_id)
            & (IxLabelArc.xlink_from == IxLabelLoc.xlink_label),
        )
        .join(
            ScLinkBaseRef,
            (ScLinkBaseRef.head_item_key == head_item_key)
            & (ScLinkBaseRef.xbrl_type == xbrl_type)
            & (IxLabelValue.source_file_id == ScLinkBaseRef.href_source_file_id),
        )
        .where(IxLabelLoc.xlink_href.in_(names))
    )
    # endregion

    # region クエリの実行
    result = session.exec(labelQuery).all()
    # endregion

    itemLst = []
    for item in result:
        treeLabel = sc.ix_global.TreeLabel(tag=item.tag, label=item.label)
        itemLst.append(treeLabel)

    # region 結果を返す
    return sc.ix_global.TreeLabels(count=len(result), data=itemLst)
    # endregion


def is_specific(session: Session, head_item_key: str):
    """特定事業会社かどうかを取得"""

    statement = select(IxNonNumeric.value).where(
        IxNonNumeric.head_item_key == head_item_key,
        IxNonNumeric.name == "tse-ed-t_SpecificBusiness",
    )
    result = session.exec(statement).first()

    if result == "true":
        return True
    else:
        return False


def get_accounting_standard(session: Session, head_item_key: str):
    """会計基準を取得"""

    statement = select(IxNonNumeric.value).where(
        IxNonNumeric.head_item_key == head_item_key,
        IxNonNumeric.name == "jpdei_cor_AccountingStandardsDEI",
    )
    result = session.exec(statement).first()

    return result


def get_tree_items(*, session: Session, head_item_key: str, xbrl_type: str) -> List:
    """ツリーアイテムを取得する"""

    NonFrac = aliased(IxNonFraction)
    NonNum = aliased(IxNonNumeric)

    # 非分数データの取得
    statement = select(NonFrac).where(
        NonFrac.head_item_key == head_item_key,
        NonFrac.xbrl_type == xbrl_type,
    )
