import os
from typing import Dict, List, Tuple

import humps
from app.api.deps import SessionDep
from app.models import IxLabelArc, IxLabelLoc, IxLabelValue, IxNonFraction, IxNonNumeric
from fastapi import APIRouter, Query
from sqlalchemy.orm import aliased as alias
from sqlmodel import select

router = APIRouter()


@router.get("/generate_class/name/", response_model=str)
def generate_name_class(
    *,
    session: SessionDep,
    report_type: str = Query(...),
    xbrl_type: str = Query(...),
    non_fraction: bool = True,
) -> str:
    """指定したレポートタイプに対応するクラスファイルを生成する

    Args:<br/>
        session (SessionDep): DBセッション<br/>
        report_type (str): レポートタイプ (edjp, edif, edus, edit, rvdf, rvfc, rejp, rrdf, rrfc, efjp)<br/>
        non_fraction (bool): 分数でないかどうか
    """
    if non_fraction:
        alias_ = alias(IxNonFraction)
        model_name = "IxNonFraction"
    else:
        alias_ = alias(IxNonNumeric)
        model_name = "IxNonNumeric"

    # _aliasからnameとlabelを取得
    statement = (
        select(alias_.name, IxLabelValue.label)
        .join(IxLabelLoc, alias_.name == IxLabelLoc.xlink_href)
        .join(IxLabelArc, IxLabelLoc.xlink_label == IxLabelArc.xlink_from)
        .join(IxLabelValue, IxLabelArc.xlink_to == IxLabelValue.xlink_label)
        .where(
            alias_.xbrl_type == xbrl_type,
            alias_.report_type == report_type,
            IxLabelValue.xlink_role == "http://www.xbrl.org/2003/role/verboseLabel",
        )
        .group_by(
            alias_.name,
            alias_.xbrl_type,
            alias_.report_type,
            IxLabelValue.label,
        )
        .order_by(alias_.name.asc())
    )
    # statementを実行
    result = session.exec(statement)
    # name_listに結果を格納
    name_list = result.all()

    # name_listの重複を削除
    name_list = list(set(name_list))

    # name_listをalias_.name昇順に並び替え
    name_list.sort(key=lambda x: x[0])

    # クラスファイルを生成
    finance_select = generate_extract_model(
        name_list, report_type, model_name, non_fraction
    )
    schema_file = generate_schema_file(name_list, report_type, model_name)

    return f"{finance_select}, {schema_file}"


def generate_extract_model(
    name_list: List[Tuple[str, str]],
    report_type: str,
    model_name: str,
    non_fraction: bool = True,
) -> str:
    """extract/{model_name}_{report_type}.pyを生成する"""
    class_name = f"{humps.decamelize(model_name)}_{report_type}"
    dir_path = "app/extract"
    file_path = f"{dir_path}/{class_name}.py"

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # ファイルが存在する場合は削除
    if os.path.exists(file_path):
        os.remove(file_path)

    def_name_list = []
    # 新しくクラスファイルを作成
    with open(file_path, "w") as f:
        f.write(f"from app.models import {model_name}\n")
        if non_fraction:
            f.write(f"from sqlmodel import Session, select, func\n")
        else:
            f.write(f"from sqlmodel import Session, select\n")
        f.write(f"\n")
        for name_dict in name_list:
            name = name_dict[0]
            label = name_dict[1]

            def_name = name.replace("tse-ed-t_", "")
            def_name = humps.decamelize(def_name)
            if def_name in def_name_list:
                continue
            def_name_list.append(def_name)
            if non_fraction:
                f.write(
                    f"def {def_name}(session: Session, head_item_key:str, context:str):\n"
                )  # 関数の定義
            else:
                f.write(f"def {def_name}(session: Session, head_item_key:str):\n")
            f.write(f'    """\n')  # docstringの開始
            f.write(f"    {label}\n")  # labelの追加
            f.write(f'    """\n')  # docstringの終了
            f.write(f"    statement = (\n")
            f.write(f"        select({model_name})\n")
            f.write(f"        .where(\n")
            f.write(f"            {model_name}.name == '{name}',\n")
            f.write(f"            {model_name}.head_item_key == head_item_key,\n")
            if non_fraction:
                f.write(
                    f"            func.regexp_match({model_name}.context, context),\n"
                )
            f.write(f"        )\n")
            f.write(f"    )\n")
            f.write(f"    result = session.exec(statement)\n")
            f.write(f"    item = result.all()\n")
            f.write(f"    if len(item) > 1:\n")
            f.write(
                f"        raise ValueError('複数のデータが取得されました。contextが不足しています。')\n"
            )
            f.write(f"    elif len(item) < 1:\n")
            f.write(f"        raise ValueError('データが取得されませんでした。')\n")
            f.write(f"    return item[0]\n")
            f.write(f"\n")

    return file_path


def generate_schema_file(
    name_list: List[Tuple[str, str]],
    report_type: str,
    model_name: str,
) -> str:
    """extract/{model_name}_{report_type}.pyを生成する"""
    model_name_snake = humps.decamelize(model_name)
    module_name = f"{model_name_snake}_{report_type}"  # ix_non_fraction_edjp
    class_name = humps.pascalize(module_name)  # IxNonFractionEdjp
    model_name_pascal = f"{humps.pascalize(model_name)}Public"  # IxNonFractionPublic
    dir_path = "app/schema"
    file_path = f"{dir_path}/{module_name}.py"

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # ファイルが存在する場合は削除
    if os.path.exists(file_path):
        os.remove(file_path)

    field_name_list = []
    # 新しくクラスファイルを作成
    with open(file_path, "w") as f:
        f.write(f"from app.models import Field, SQLModel\n")
        f.write(f"from app.schema.{model_name_snake} import {model_name_pascal}\n")
        f.write(f"from typing import Optional\n")
        f.write(f"\n")
        f.write(f"class {class_name}(SQLModel):\n")
        for name_dict in name_list:
            name = name_dict[0]
            label = name_dict[1]

            field_name = name.replace("tse-ed-t_", "")
            field_name = humps.decamelize(field_name)
            if field_name in field_name_list:
                continue
            field_name_list.append(field_name)
            f.write(
                f"    {field_name}: Optional[{model_name_pascal}] = Field(default=None, description='{label}')\n"
            )
            f.write(f'    """ {label} """\n')
        f.write(f"\n")

    return file_path


@router.get("/generate_class/context/", response_model=str)
def generate_context_class(
    *,
    session: SessionDep,
    report_type: str = Query(...),
    xbrl_type: str = Query(...),
    non_fraction: bool = True,
) -> str:
    """指定したレポートタイプに対応するクラスファイルを生成する (context用)"""

    if non_fraction:
        alias_ = alias(IxNonFraction)
        model_name = "IxNonFraction"
    else:
        alias_ = alias(IxNonNumeric)
        model_name = "IxNonNumeric"

    statement = (
        select(alias_.name, alias_.context)
        .where(
            alias_.xbrl_type == xbrl_type,
            alias_.report_type == report_type,
        )
        .group_by(
            alias_.name,
            alias_.xbrl_type,
            alias_.report_type,
            alias_.context,
        )
        .order_by(alias_.context.asc())
    )
    # statementを実行
    result = session.exec(statement)
    # name_listに結果を格納
    name_list = result.all()

    # name_listの重複を削除
    name_list = list(set(name_list))

    # name,contextで昇順ソート
    name_list.sort(key=lambda x: (x[0], x[1]))

    # name_listをnameをキーとした辞書に変換
    name_dict = {}
    for name, context in name_list:
        if name in name_dict:
            name_dict[name].append(context)
        else:
            name_dict[name] = [context]

    # クラスファイルを生成
    context_file = generate_context_file(name_dict, report_type, model_name)

    return context_file


def generate_context_file(
    name_list: Dict[str, List[str]],
    report_type: str,
    model_name: str,
) -> str:
    """extract/{model_name}_{report_type}.pyを生成する"""
    context_label = {
        "CurrentYearDuration": "当年度会計期間",
        "CurrentAccumulatedQ1Duration": "当年度期初から第１四半期間",
        "CurrentAccumulatedQ2Duration": "当年度期初から第２四半期間",
        "CurrentAccumulatedQ3Duration": "当年度期初から第３四半期間",
        "NextYearDuration": "次年度会計期間",
        "Next2YearDuration": "次々年度会計期間",
        "NextAccumulatedQ1Duration": "次年度期初から第１四半期間",
        "NextAccumulatedQ2Duration": "次年度期初から第２四半期間",
        "NextAccumulatedQ3Duration": "次年度期初から第３四半期間",
        "PriorYearDuration": "前年度会計期間",
        "PriorAccumulatedQ1Duration": "前年度期初から第１四半期間",
        "PriorAccumulatedQ2Duration": "前年度期初から第２四半期間",
        "PriorAccumulatedQ3Duration": "前年度期初から第３四半期間",
        "CurrentYearInstant": "当年度時点",
        "CurrentAccumulatedQ1Instant": "当年度期初から第１四半期間時点",
        "CurrentAccumulatedQ2Instant": "当年度期初から第２四半期間時点",
        "CurrentAccumulatedQ3Instant": "当年度期初から第３四半期間時点",
        "NextYearInstant": "次年度時点",
        "Next2YearInstant": "次々年度時点",
        "NextAccumulatedQ1Instant": "次年度期初から第１四半期間時点",
        "NextAccumulatedQ2Instant": "次年度期初から第２四半期間時点",
        "NextAccumulatedQ3Instant": "次年度期初から第３四半期間時点",
        "PriorYearInstant": "前年度時点",
        "PriorAccumulatedQ1Instant": "前年度期初から第１四半期間時点",
        "PriorAccumulatedQ2Instant": "前年度期初から第２四半期間時点",
        "PriorAccumulatedQ3Instant": "前年度期初から第３四半期間時点",
    }
    model_name_snake = humps.decamelize(model_name)
    module_name = f"{model_name_snake}_{report_type}"  # ix_non_fraction_edjp
    dir_path = "app/context"
    file_path = f"{dir_path}/{module_name}.py"

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # ファイルが存在する場合は削除
    if os.path.exists(file_path):
        os.remove(file_path)

    # 新しくクラスファイルを作成
    with open(file_path, "w") as f:
        f.write(f"from enum import Enum\n")
        f.write(f"\n")
        for name, context_list in name_list.items():
            f.write(f"class {name.replace('tse-ed-t_','')}(Enum):\n")
            for context in context_list:
                f.write(f"    {humps.decamelize(context).upper()} = '{context}'\n")
            f.write(f"\n")
            f.write(f"\n")

    return file_path
