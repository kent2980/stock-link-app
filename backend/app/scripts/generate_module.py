import os
from typing import Any, Dict, List, Tuple

import alembic
import humps
import requests


def generate_extract_model(
    name_list: List[Tuple[str, str]],
    report_type: str,
    xbrl_type: str,
    non_fraction: bool = True,
) -> str:
    """extract/{model_name}_{report_type}.pyを生成する"""

    print(f"generate_extract_model: {report_type}, {xbrl_type}, {non_fraction}")

    if non_fraction:
        model_name = "IxNonFraction"
    else:
        model_name = "IxNonNumeric"
    class_name = f"{humps.decamelize(model_name)}_{report_type}_{xbrl_type}"
    dir_path = "../extract"
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

            def_name = name.split("_")[1:][-1]
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
            f.write(f"            {model_name}.context == context,\n")
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
    context_list: Dict[Any, Any],
    report_type: str,
    xbrl_type: str,
    non_fraction: bool = True,
) -> str:
    """extract/{model_name}_{report_type}.pyを生成する"""

    print(f"generate_schema_file: {report_type}, {xbrl_type}, {non_fraction}")

    if non_fraction:
        model_name = "IxNonFraction"
    else:
        model_name = "IxNonNumeric"
    model_name_snake = humps.decamelize(model_name)
    module_name = (
        f"{model_name_snake}_{report_type}_{xbrl_type}"  # ix_non_fraction_edjp
    )
    class_name = humps.pascalize(module_name)  # IxNonFractionEdjp
    model_name_pascal = f"{humps.pascalize(model_name)}Public"  # IxNonFractionPublic
    dir_path = "../schema"
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

            field_name = name.split("_")[1:][-1]
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


def generate_context_file(
    name_list: Dict[Any, Any],
    report_type: str,
    xbrl_type: str,
    non_fraction: bool = True,
) -> str:
    """extract/{model_name}_{report_type}.pyを生成する"""

    print(f"generate_context_file: {report_type}, {xbrl_type}, {non_fraction}")

    if non_fraction:
        model_name = "IxNonFraction"
    else:
        model_name = "IxNonNumeric"

    model_name_snake = humps.decamelize(model_name)
    module_name = (
        f"{model_name_snake}_{report_type}_{xbrl_type}"  # ix_non_fraction_edjp
    )
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
            f.write(f"class {name.split('_')[-1]}(Enum):\n")  # Enumの定義
            if len(context_list["label"]) > 0:
                f.write(f'    """"{context_list["label"]}"""\n')  # docstringの開始
            for context in context_list["item"]:
                try:
                    context_value = context["context"]
                except KeyError:
                    print("KeyError")
                    print(context)
                    continue
                context_snake = humps.decamelize(context_value)
                f.write(
                    f"    {context_snake.upper().replace("-","_")} = '{context['context']}'\n"
                )  # 関数の定義
                if len(context["label"]) > 0:
                    f.write(f'    """ {context['label']} """\n')  # docstringの開始
            f.write(f"\n")
            f.write(f"\n")

    return file_path


if __name__ == "__main__":
    API_BASE_URL = "http://localhost:8000/api/v1"
    API_ENDPOINTS = {
        "name": "/generate/grouping/names/",
        "context": "/generate/grouping/contexts/",
    }
    # 引数から値を取得
    report_types = ["edjp", "edif", "edus", "rvfc"]
    xbrl_types = ["sm", "fr"]
    non_fractions = [True, False]

    for report_type in report_types:
        for xbrl_type in xbrl_types:
            for non_fraction in non_fractions:
                # データを取得
                name_response = requests.get(
                    f"{API_BASE_URL}{API_ENDPOINTS['name']}",
                    params={
                        "report_type": report_type,
                        "xbrl_type": xbrl_type,
                        "non_fraction": non_fraction,
                    },
                )

                name_list = name_response.json()

                if len(name_list) == 0:
                    continue

                # ファイルを生成
                extract_file_path = generate_extract_model(
                    name_list, report_type, xbrl_type, non_fraction
                )

                # contextを取得
                context_response = requests.get(
                    f"{API_BASE_URL}{API_ENDPOINTS['context']}",
                    params={
                        "report_type": report_type,
                        "xbrl_type": xbrl_type,
                        "non_fraction": non_fraction,
                    },
                )

                context_list = context_response.json()

                if len(context_list) == 0:
                    continue

                context_file_path = generate_context_file(
                    context_list, report_type, xbrl_type, non_fraction
                )

                schema_file_path = generate_schema_file(
                    name_list, context_list, report_type, xbrl_type, non_fraction
                )
