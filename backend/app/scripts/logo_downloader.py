import json
import os
import re
from time import sleep
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs
from requests.exceptions import ConnectTimeout, SSLError


def save_file(
    file_path: str,
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
    print(f"{type}ファイルを保存しました: {file_path}.{type}")
    return file_full_path


def safe_get(url, timeout=10):
    """
    HTTPリクエストを安全に実行し、HTTPで失敗した場合にHTTPSで再試行します。
    :param url: リクエストするURL
    :param timeout: タイムアウト時間
    :return: レスポンスオブジェクトまたはNone
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # ステータスコードがエラーの場合例外を発生
        return response
    except (ConnectTimeout, SSLError) as e:
        print(f"HTTPでエラーが発生しました。HTTPSで再試行します: {url}")
        if url.startswith("http://"):
            https_url = url.replace("http://", "https://", 1)
            try:
                response = requests.get(https_url, timeout=timeout)
                response.raise_for_status()
                return response
            except Exception as https_error:
                print(
                    f"HTTPSでもエラーが発生しました: {https_url}, エラー: {https_error}"
                )
        else:
            print(f"HTTPSリトライができません: {url}")
    except Exception as e:
        print(f"リクエスト中にエラーが発生しました: {url}, エラー: {e}")
    return None


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

    # GETリクエストを送信してHTMLを取得
    response = safe_get(url)
    if not response:
        print(f"リクエストに失敗しました: {url}")
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
            return save_file(file_path, str(svg), "svg", "w", encoding="utf-8")
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

        # データURIスキームの場合の処理
        if logo_url.startswith("data:"):
            # データURIを分割してデータ部分を取得
            header, encoded = logo_url.split(",", 1)
            if "image/svg+xml" in header:
                # SVGデータをデコードして保存
                svg_data = encoded
                return save_file(file_path, svg_data, "svg", "w", encoding="utf-8")
            elif "base64" in header:
                # Base64デコードしてバイナリデータを保存
                image_data = base64.b64decode(encoded)
                extension = header.split(";")[0].split("/")[
                    1
                ]  # MIMEタイプから拡張子を取得
                return save_file(file_path, image_data, extension, "wb")
            else:
                print(f"未対応のデータURI形式: {header}")
                return None

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
                return save_file(
                    file_path, logo_response.text, "svg", "w", encoding="utf-8"
                )
            # 拡張子がwebpの場合は、WEBPとして保存
            elif re.match(r".*\.webp$", logo_url):
                return save_file(file_path, logo_response.content, "webp", "wb")
            # 拡張子がpngの場合は、PNGとして保存
            elif re.match(r".*\.png.*", logo_url):
                return save_file(file_path, logo_response.content, "png", "wb")
            # 拡張子がjpgまたはjpegの場合は、JPEGとして保存
            elif re.match(r".*\.jpg.*|.*\.jpeg.*", logo_url):
                return save_file(file_path, logo_response.content, "jpg", "wb")
            # 拡張子がgifの場合は、GIFとして保存
            elif re.match(r".*\.gif.*", logo_url):
                return save_file(file_path, logo_response.content, "gif", "wb")
        else:
            print(
                f"エラーが発生したため、保存できませんでした。: {logo_response.status_code}"
            )

    print(f"ロゴファイルが見つかりませんでした。file_name: {filename}, url: {url}")
    return None


if __name__ == "__main__":

    if len(os.sys.argv) > 1:
        # コマンドライン引数が指定された場合
        api_base = os.sys.argv[1]

    api_url = f"{api_base}/api/v1/xbrl/url_list/"
    directory = "../frontend/public/assets/images/stock_logo/"
    parrentDir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    json_output_dir = f"{parrentDir}/frontend/src/logo/"
    json_path = os.path.join(json_output_dir, "logo_list.json")

    # 処理の開始時に logo_list.json を初期化
    os.makedirs(json_output_dir, exist_ok=True)
    if not os.path.exists(json_path):
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for item in data["data"]:
            url = item["url"]
            securities_code = item["securities_code"]
            filename = f"{securities_code}_logo"

            # ファイルが存在するか確認
            file_path = os.path.join(directory, filename)
            existing_file = None
            for ext in ["svg", "png", "jpg", "jpeg", "gif", "webp"]:
                if os.path.exists(f"{file_path}.{ext}"):
                    existing_file = f"{filename}.{ext}"
                    break

            # ファイルが存在する場合でも logo_list.json に追記
            if existing_file:
                print(f"ファイルが存在するため、スキップしました: {existing_file}")
                with open(json_path, "r+", encoding="utf-8") as f:
                    file_data = json.load(f)
                    file_data.append(
                        {
                            "code": securities_code,
                            "file_name": existing_file,
                        }
                    )
                    f.seek(0)
                    json.dump(file_data, f, ensure_ascii=False, indent=4)
                continue

            # ファイルをダウンロードして保存
            output = download_logo(url, directory, filename)
            if output:
                with open(json_path, "r+", encoding="utf-8") as f:
                    file_data = json.load(f)
                    file_data.append(
                        {
                            "code": securities_code,
                            "file_name": f"{filename}.{output.split('.')[-1]}",
                        }
                    )
                    f.seek(0)
                    json.dump(file_data, f, ensure_ascii=False, indent=4)
    else:
        print(f"Failed to fetch URLs. Status code: {response.status_code}")
