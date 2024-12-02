import json
import os

import humps


def create_class_module(file_path: str):
    """クラスモジュールを生成します。

    Args:
        file_path (str): ファイルパス
    """

    with open(file_path, "w") as f:  # ファイルを新規作成モードで開く
        f.write(f"from app.models import Field, SQLModel\n")
        f.write("from app.schema.ix_non_numeric import IxNonNumericPublic\n")
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
            for v in value:
                name = v["name"]
                label = v["label"]
                f.write(
                    f"    {humps.depascalize(name.split('_')[-1]).replace('__','_')}:IxNonNumericPublic = Field(default=None, description=\"{label}\")\n"
                )
                f.write(f'    """ {label} """\n')

            f.write("\n\n")


def generate_schema_link_class(data: dict, kwd: str):
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../../utils/schema_class_non_numeric.py")
    with open(json_path, "w") as f:  # ファイルを新規作成モードで開く
        f.write("import app.schema.ix_summary_non_numeric as sc\n")
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
            if count == 0:
                f.write(f"    sc.{key}\n")
            else:
                f.write(f"    | sc.{key}\n")
            count += 1
        f.write("    )\n")
        f.write("    return items\n")


def generate_schema():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../../json/non_numeric/grouped_data.json")
    with open(json_path, "r") as f:
        data = json.load(f)

    schema_path = os.path.join(base_dir, "../../schema/ix_summary_non_numeric.py")
    create_class_module(schema_path)
    write_key_schema(schema_path, data)
    generate_schema_link_class(data, "FinancialReportSummary")


if __name__ == "__main__":
    generate_schema()
