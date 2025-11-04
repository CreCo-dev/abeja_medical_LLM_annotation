# API Interface Definitions

このディレクトリには、バックエンドAPIのOpenAPI仕様書が格納されています。

## ファイル

- `openapi.json` - OpenAPI 3.1.0仕様（JSON形式）
- `openapi.yaml` - OpenAPI 3.1.0仕様（YAML形式）

## 使用方法

### 1. TypeScript型定義の自動生成

フロントエンド開発で使用するTypeScript型定義を自動生成できます。

```bash
# openapi-typescript を使用
npx openapi-typescript interface/openapi.yaml -o frontend/src/types/api.ts

# または openapi-generator を使用
npx @openapitools/openapi-generator-cli generate \
  -i interface/openapi.yaml \
  -g typescript-fetch \
  -o frontend/src/generated
```

### 2. APIクライアントの自動生成

```bash
# axios ベースのクライアント生成
npx @openapitools/openapi-generator-cli generate \
  -i interface/openapi.yaml \
  -g typescript-axios \
  -o frontend/src/api-client
```

### 3. APIドキュメントの閲覧

FastAPIが提供する自動ドキュメントを使用：

- Swagger UI: http://localhost:80/docs
- ReDoc: http://localhost:80/redoc

### 4. 仕様書の更新

バックエンドのAPIを変更した後、以下のコマンドで仕様書を更新できます：

```bash
# バックエンドが起動している状態で
curl http://localhost:80/openapi.json > interface/openapi.json

# YAML形式に変換（yq が必要）
yq eval -P interface/openapi.json > interface/openapi.yaml
```

## 利点

- **型安全性**: TypeScript型定義により、コンパイル時にAPIの型チェックが可能
- **自動補完**: IDEでAPIのパラメータやレスポンスの自動補完が効く
- **ドキュメント**: APIの仕様が常に最新の状態で共有される
- **テスト**: OpenAPI仕様を使ったAPIテストの自動化が可能
