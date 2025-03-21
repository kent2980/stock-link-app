import json
import os

import humps

import app.utils.summary as summary


def create_class_module(file_path: str):
    """クラスモジュールを生成します。

    Args:
        file_path (str): ファイルパス
    """

    with open(file_path, "w") as f:  # ファイルを新規作成モードで開く
        f.write(f"from app.models import Field, SQLModel\n")
        f.write("from app.schema.ix_non_fraction import IxNonFractionPublic\n")
        # f.write("\n\n")
        # f.write("class IxbrlBase(SQLModel):\n")
        # f.write('    type: str = Field(default=None, description="識別キー")\n\n')
        # f.write("    def __init__(self, **kwargs):\n")
        # f.write("        super().__init__(**kwargs)\n")
        # f.write("        self.type = self.__class__.__name__\n")
        f.write("\n\n")


def write_key_schema(file_path: str, data: dict):
    with open(file_path, "a") as f:  # ファイルを追記モードで開く
        for key, value in data.items():
            f.write(f"class {key}(SQLModel):\n")
            f.write(f'    type: str = Field(default="{key}", description="型タイプ")\n')
            f.write('    """ 型タイプ """\n')
            for k, v in value.items():
                f.write(
                    f"    {humps.depascalize(k.split('_')[-1]).replace('__','_')}:{k.split('_')[-1]}_{key} = Field(default=None, description=\"{v['label']}\")\n"
                )
                f.write(f'    """ {v["label"]} """\n')

            f.write("\n\n")


def write_name_schema(file_path: str, data: dict):

    add_list = []
    with open(file_path, "a") as f:  # ファイルを追記モードで開く
        for key, value in data.items():
            for k, v in value.items():
                if f"{k.split('_')[-1]}_{key}" not in add_list:
                    f.write(f"class {k.split('_')[-1]}_{key}(SQLModel):\n")
                    f.write(f'    """ {v["label"]} """\n\n')
                    for item in v["item"]:
                        f.write(
                            f"    {summary.get_short_context(item['context'])}: IxNonFractionPublic = Field(default=None, description=\"{item['context_label']}\")\n"
                        )
                        f.write(f'    """ {item["context_label"]} """\n')
                    add_list.append(f"{k.split('_')[-1]}_{key}")

                    f.write("\n\n")


def generate_schema_link_class(data: dict, kwd: str):
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../../utils/schema_class_non_fraction.py")
    with open(json_path, "w") as f:  # ファイルを新規作成モードで開く
        f.write("import app.schema.ix_summary_non_fraction as sc\n")
        f.write("\n\n")
        f.write("def get_schema_class(key: str):\n")
        for key in data.keys():
            f.write(f'    if key == "{key}":\n')
            f.write(f"        return sc.{key}\n")
        f.write("\n\n")
        f.write(f"def get_response_schema_{kwd}_class():\n")
        f.write("    items = (\n")
        count = 0
        for key in data.keys():
            if kwd in key:
                if count == 0:
                    f.write(f"    sc.{key}\n")
                else:
                    f.write(f"    | sc.{key}\n")
                count += 1
        f.write("    )\n")
        f.write("    return items\n")


def generate_schema():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../../json/non_fraction/name_context.json")
    with open(json_path, "r") as f:
        data = json.load(f)

    schema_path = os.path.join(base_dir, "../../schema/ix_summary_non_fraction.py")
    create_class_module(schema_path)
    write_name_schema(schema_path, data)
    write_key_schema(schema_path, data)
    generate_schema_link_class(data, "FinancialReportSummary")


if __name__ == "__main__":
    generate_schema()
