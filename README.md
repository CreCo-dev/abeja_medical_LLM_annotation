# abeja_medical_LLM_annotation

# バックエンド
## 環境構築
- (Dockerのインストール)
- cd abeja_medical_LLM_annotation
- docker compose up --build
## doc
- http://localhost:80/docs
- http://localhost:80/redoc
## テスト
- curl http://localhost:80/
- curl -X GET http://localhost:80/sample_get
- curl -X POST http://localhost:80/sample_post
## データベース
- user_accounts
    | カラム名 | 型 | 制約 |
    | -------------- | ---------------- | ------------------------------------------ |
    | `id`           | `INTEGER`        | `PRIMARY KEY`, `AUTO INCREMENT`, `INDEX`   |
    | `login_id`     | `VARCHAR(50)`    | `UNIQUE`, `NOT NULL`                       |
    | `password`     | `VARCHAR(255)`   | `NOT NULL`                                 |
    | `name`         | `VARCHAR(50)`    | `NOT NULL`                                 |


# フロントエンド
