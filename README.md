# abeja_medical_LLM_annotation

# バックエンド
## Dockerの場合
### 環境構築
- (Dockerのインストール)
- cd abeja_medical_LLM_annotation
- docker compose up --build
### doc
- http://localhost:80/docs
- http://localhost:80/redoc
### テスト
- curl http://localhost:80/
- curl -X GET http://localhost:80/sample_get
- curl -X POST http://localhost:80/sample_post

## ローカルの場合
### 環境構築
- (Python3のインストール)
- (pip3のインストール)
- pip3 install fastapi uvicorn
- cd ./fastapi_sample/app
- uvicorn main:app --reload
### doc
- http://localhost:8000/docs
- http://localhost:8000/redoc
### テスト
- curl http://localhost:8000/
- curl -X GET http://localhost:8000/sample_get
- curl -X POST http://localhost:8000/sample_post


# フロントエンド
