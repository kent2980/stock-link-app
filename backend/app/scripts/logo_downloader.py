import json
import os
import re
from time import sleep
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs
from requests.exceptions import SSLError,ConnectTimeout


def download_logo(url, directory, filename) -> Optional[str]:
    """
    Download the logo from the given URL and save it to a file.
    """

    # ファイルが存在する場合は処理をスキップ
    file_path = os.path.join(directory, filename)
    if (
        os.path.exists(file_path + ".svg")
        or os.path.exists(file_path + ".png")
        or os.path.exists(file_path + ".jpg")
        or os.path.exists(file_path + ".jpeg")
        or os.path.exists(file_path + ".gif")
        or os.path.exists(file_path + ".webp")
    ):
        return None

    # 待機時間を設定
    sleep(2)

    # ディレクトリが存在しない場合は作成
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, filename)

    def save_file(
        content,
        type: str,
        mode,
        encoding=None,
    ):
        """
        指定された拡張子でファイルを保存する
        :param content: 保存する内容
        :param type: 拡張子
        :param mode: モード
        :param encoding: エンコーディング
        """
        # 相対パスを絶対パスに変換
        file_full_path = os.path.abspath(os.path.join(file_path + "." + type))
        with open(file_full_path, mode, encoding=encoding) as f:
            f.write(content)
        print(f"{type}ファイルを保存しました: {filename}.{type},url: {url}")
        return file_full_path

    # GETリクエストを送信してHTMLを取得
    try:
        response = requests.get(url)
    except SSLError:
        print(f"SSLエラーが発生しました: file_name: {filename}, url: {url}")
        return None
    except ConnectTimeout:
        print(f"接続タイムアウトエラーが発生しました: file_name: {filename}, url: {url}")
        return None

    # ステータスコードが200でない場合はエラー
    if response.status_code != 200:
        print(
            f"レスポンスエラーが発生しました: file_name: {filename}, url: {url}, status_code: {response.status_code}"
        )
        return None

    # BeautifulSoupでHTMLを解析
    bs_obj = bs(response.content, "html.parser")

    # imgタグを探す
    logo_class = bs_obj.find(class_=re.compile(".*logo.*"))
    logo = None
    if logo_class:
        logo = logo_class.find("img")
        print("logo_classからimgを取得")
    else:
        logo_class = bs_obj.find("header")
        # headerタグ内のimgタグを探す
        if logo_class:
            logo = logo_class.find("img")
            print("headerからimgを取得")
    if not logo:
        svg = bs_obj.find(
            "svg", class_=lambda class_name: class_name and "mobile" not in class_name
        )
        if svg:
            return save_file(str(svg), "svg", "w", encoding="utf-8")
        else:
            logo = bs_obj.find("img")
            print("imgを取得")

    # logoが見つかった場合
    if logo:
        try:
            # data-src属性を優先して取得
            logo_url = logo["data-src"]
        except KeyError:
            # data-src属性がない場合はsrc属性を取得
            logo_url = logo["src"]

        # 取得したURLが相対パスの場合は、絶対URLに変換
        if not logo_url.startswith("http"):
            logo_url = urljoin(url, logo_url)

        # 画像をダウンロード
        logo_response = requests.get(logo_url)
        print(f"logo_url: {logo_url}")
        # ステータスコードが200でない場合はエラー
        if logo_response.status_code == 200:
            # 拡張子がsvgの場合は、SVGとして保存
            if re.match(r".*\.svg.*", logo_url):
                return save_file(logo_response.text, "svg", "w", encoding="utf-8")
            # 拡張子がwebpの場合は、WEBPとして保存
            elif re.match(r".*\.webp$", logo_url):
                return save_file(logo_response.content, "webp", "wb")
            # 拡張子がpngの場合は、PNGとして保存
            elif re.match(r".*\.png.*", logo_url):
                return save_file(logo_response.content, "png", "wb")
            # 拡張子がjpgまたはjpegの場合は、JPEGとして保存
            elif re.match(r".*\.jpg.*|.*\.jpeg.*", logo_url):
                return save_file(logo_response.content, "jpg", "wb")
            # 拡張子がgifの場合は、GIFとして保存
            elif re.match(r".*\.gif.*", logo_url):
                return save_file(logo_response.content, "gif", "wb")
        else:
            print(
                f"エラーが発生したため、保存できませんでした。: {logo_response.status_code}"
            )

    print(f"ロゴファイルが見つかりませんでした。file_name: {filename}, url: {url}")


if __name__ == "__main__":

    api_url = "http://157.7.78.166/api/v1/xbrl/url_list/"
    directory = "../frontend/public/assets/images/stock_logo/"
    json_output_dir = "../frontend/src/logo/"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for item in data["data"]:
            url = item["url"]
            securities_code = item["securities_code"]
            filename = f"{securities_code}_logo"
            output = download_logo(url, directory, filename)
    else:
        print(f"Failed to fetch URLs. Status code: {response.status_code}")

    # directory内のファイルをリストで取得
    files = os.listdir(directory)

    # ファイル名と拡張子を分割して DataFrame を作成
    file_data = []
    for file in files:
        file_split = file.rsplit(".", 1)  # 拡張子が存在しない場合を考慮
        if len(file_split) == 2:
            file_name, file_ext = file_split
        else:
            file_name, file_ext = file_split[0], ""  # 拡張子がない場合は空文字列
        file_data.append(
            {
                "code": file_name.replace("_logo", ""),
                "file_name": file,
            }
        )
    json_path = os.path.join(json_output_dir, "logo_list.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(file_data, f, ensure_ascii=False, indent=4)
