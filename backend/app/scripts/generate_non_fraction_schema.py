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
        f.write("from app.schema.ix_non_fraction import IxNonFractionPublic\n")
        f.write("\n\n")


def write_key_schema(file_path: str, data: dict):
    with open(file_path, "a") as f:  # ファイルを追記モードで開く
        for key, value in data.items():
            f.write(f"class {key}(SQLModel):\n")
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
                            f"    {humps.depascalize(item['context']).replace('__','_')}: IxNonFractionPublic = Field(default=None, description=\"{item['context_label']}\")\n"
                        )
                        f.write(f'    """ {item["context_label"]} """\n')
                    add_list.append(f"{k.split('_')[-1]}_{key}")

                    f.write("\n\n")


def generate_schema():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "../json/non_fraction_name_context.json")
    with open(json_path, "r") as f:
        data = json.load(f)

    schema_path = os.path.join(base_dir, "../schema/ix_summary.py")
    create_class_module(schema_path)
    write_name_schema(schema_path, data)
    write_key_schema(schema_path, data)


if __name__ == "__main__":
    generate_schema()
