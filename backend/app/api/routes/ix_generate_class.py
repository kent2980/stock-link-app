import os
from typing import List, Tuple

import humps
from app.api.deps import SessionDep
from app.models import IxLabelArc, IxLabelLoc, IxLabelValue, IxNonFraction, IxNonNumeric
from fastapi import APIRouter, Query
from sqlalchemy.orm import aliased as alias
from sqlmodel import select

router = APIRouter()


@router.post("/generate_class/", response_model=str)
def generate_class(
    *, session: SessionDep, report_type: str = Query(...), non_fraction: bool = True
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
            alias_.xbrl_type == "sm",
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
            f.write(
                f"def {def_name}(*, session: Session, head_item_key:str, context:str):\n"
            )  # 関数の定義
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
            f.write(f"    item = result.first()\n")
            f.write(f"    if item:\n")
            f.write(f"        return item\n")
            f.write(f"    return None\n")
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
