import os
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs


def download_logo(url, directory, filename) -> Optional[str]:
    """
    Download the logo from the given URL and save it to a file.
    """

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
        with open(file_path + "." + type, mode, encoding=encoding) as f:
            f.write(content)
        print(f"{type}ファイルを保存しました: {filename}.{type}")
        return file_path + "." + type

    # GETリクエストを送信してHTMLを取得
    response = requests.get(url)

    # ステータスコードが200でない場合はエラー
    if response.status_code != 200:
        print(f"Failed to download logo. Status code: {response.status_code}")

    # BeautifulSoupでHTMLを解析
    bs_obj = bs(response.content, "html.parser")

    # SVGを探す
    svg = bs_obj.find("svg")
    if svg:
        return save_file(str(svg), "svg", "w", encoding="utf-8")

    else:
        # imgタグを探す
        logo_class = bs_obj.find("header")
        logo = bs_obj.find("img")
        # logo_classが存在する場合は、logo_class内のimgタグを探す
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

            # ステータスコードが200でない場合はエラー
            if logo_response.status_code == 200:
                # 拡張子がsvgの場合は、SVGとして保存
                if logo_url.endswith(".svg"):
                    return save_file(logo_response.text, "svg", "w", encoding="utf-8")
                # 拡張子がpngの場合は、PNGとして保存
                elif logo_url.endswith(".png"):
                    return save_file(logo_response.content, "png", "wb")
                # 拡張子がjpgまたはjpegの場合は、JPEGとして保存
                elif logo_url.endswith(".jpg") or logo_url.endswith(".jpeg"):
                    return save_file(logo_response.content, "jpg", "wb")
            else:
                print(
                    f"エラーが発生したため、保存できませんでした。: {logo_response.status_code}"
                )

    print("ロゴファイルが見つかりませんでした")


if __name__ == "__main__":
    # Example usage
    url = "https://www.opto.co.jp/"  # Replace with the URL of the page containing the logo
    directory = "logo"  # Replace with the desired directory to save the logo
    filename = "logo"  # Replace with the desired filename for the logo image

    download_logo(url, directory, filename)
