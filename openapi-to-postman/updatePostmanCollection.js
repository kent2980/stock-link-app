"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var axios_1 = require("axios");
var fs = require("fs");
var openapiToPostman = require("openapi-to-postmanv2");
var util_1 = require("util");
var readFileAsync = (0, util_1.promisify)(fs.readFile);
var convertAsync = (0, util_1.promisify)(openapiToPostman.convert);
// Postman APIキーとコレクションID、ワークスペースIDを設定
var apiKey = "PMAK-67a9fea28e4dbb0001be6025-ce3f2ca5ba99421e91008b72a0cd45a4c2";
var collectionId = "25361473-fa50396c-0934-4cd6-a8eb-92f7c99054b5";
var workspaceId = "bedc640a-9748-4cc3-8d5d-38feee02bbd7";
// OpenAPI JSONファイルのパス
var openApiFileUrl = "http://localhost:8000/api/v1/openapi.json";
var openApiFilePath = "/Users/user/Vscode/XBRL_Parse_Project/stock-link-app/openapi-to-postman/doc/openapi.json";
function updatePostmanCollection() {
    return __awaiter(this, void 0, void 0, function () {
        var openApiData, conversionResult, reason, collectionData, url, headers, response, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    // OpenAPI JSONファイルをダウンロード
                    axios_1.default
                        .get(openApiFileUrl)
                        .then(function (response) {
                        fs.writeFileSync(openApiFilePath, JSON.stringify(response.data));
                    })
                        .catch(function (error) {
                        console.error("エラーが発生しました:", error);
                    });
                    _a.label = 1;
                case 1:
                    if (!!fs.existsSync(openApiFilePath)) return [3 /*break*/, 3];
                    return [4 /*yield*/, new Promise(function (resolve) { return setTimeout(resolve, 1000); })];
                case 2:
                    _a.sent();
                    return [3 /*break*/, 1];
                case 3:
                    _a.trys.push([3, 7, , 8]);
                    return [4 /*yield*/, readFileAsync(openApiFilePath, "utf8")];
                case 4:
                    openApiData = _a.sent();
                    return [4 /*yield*/, convertAsync({ type: "string", data: openApiData }, {})];
                case 5:
                    conversionResult = _a.sent();
                    if (!conversionResult.result) {
                        reason = conversionResult.reason || "不明なエラー";
                        throw new Error("\u5909\u63DB\u306B\u5931\u6557\u3057\u307E\u3057\u305F: ".concat(reason));
                    }
                    collectionData = conversionResult.output[0].data;
                    url = "https://api.getpostman.com/collections/" + collectionId;
                    headers = {
                        "Content-Type": "application/json",
                        "X-API-Key": apiKey,
                    };
                    return [4 /*yield*/, axios_1.default.put(url, { collection: collectionData }, { headers: headers })];
                case 6:
                    response = _a.sent();
                    if (response.status === 200) {
                        console.log("コレクションが正常に更新されました。");
                    }
                    else {
                        console.error("\u30A8\u30E9\u30FC\u304C\u767A\u751F\u3057\u307E\u3057\u305F: ".concat(response.status));
                        console.error(response.data);
                    }
                    return [3 /*break*/, 8];
                case 7:
                    error_1 = _a.sent();
                    console.error("エラーが発生しました:", error_1);
                    return [3 /*break*/, 8];
                case 8: return [2 /*return*/];
            }
        });
    });
}
updatePostmanCollection();
