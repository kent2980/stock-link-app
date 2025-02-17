import axios from "axios";
import * as fs from "fs";
import * as openapiToPostman from "openapi-to-postmanv2";
import { promisify } from "util";

const readFileAsync = promisify(fs.readFile);
const convertAsync = promisify(openapiToPostman.convert);

// Postman APIキーとコレクションID、ワークスペースIDを設定
const apiKey =
  "PMAK-67a9fea28e4dbb0001be6025-ce3f2ca5ba99421e91008b72a0cd45a4c2";
const collectionId = "25361473-fa50396c-0934-4cd6-a8eb-92f7c99054b5";
const workspaceId = "bedc640a-9748-4cc3-8d5d-38feee02bbd7";

// OpenAPI JSONファイルのパス
const openApiFileUrl = "http://localhost:8000/api/v1/openapi.json";

const openApiFilePath =
  "/Users/user/Vscode/XBRL_Parse_Project/stock-link-app/openapi-to-postman/doc/openapi.json";

async function updatePostman() {
  // OpenAPI JSONファイルをダウンロード
  axios
    .get(openApiFileUrl)
    .then((response) => {
      fs.writeFileSync(openApiFilePath, JSON.stringify(response.data));
    })
    .catch((error) => {
      console.error("エラーが発生しました:", error);
    });

  // OpenAPI JSONファイルがダウンロードされるまで待機
  while (!fs.existsSync(openApiFilePath)) {
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }

  try {
    // OpenAPI JSONファイルをurlから読み込む
    const openApiData = await readFileAsync(openApiFilePath, "utf8");

    // OpenAPIをPostmanコレクションに変換
    const conversionResult = await convertAsync(
      { type: "string", data: openApiData },
      {}
    );
    if (!conversionResult.result) {
      const reason = (conversionResult as any).reason || "不明なエラー";
      throw new Error(`変換に失敗しました: ${reason}`);
    }

    const collectionData = conversionResult.output[0].data;

    // Postman APIエンドポイント
    const url = "https://api.getpostman.com/collections/" + collectionId;

    // ヘッダー情報
    const headers = {
      "Content-Type": "application/json",
      "X-API-Key": apiKey,
    };

    // PUTリクエストでコレクションを更新
    const response = await axios.put(
      url,
      { collection: collectionData },
      { headers }
    );

    if (response.status === 200) {
      console.log("コレクションが正常に更新されました。");
    } else {
      console.error(`エラーが発生しました: ${response.status}`);
      console.error(response.data);
    }
  } catch (error) {
    console.error("エラーが発生しました:", error);
  }
}

updatePostman();
