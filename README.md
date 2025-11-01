# abeja_medical_LLM_annotation

# バックエンド
## 環境構築
- (Python3のインストール)
- (pip3のインストール)
- pip3 install fastapi uvicorn
- cd fastapi_sample/app
- uvicorn main:app --reload
## doc
- http://localhost:8000/docs
- http://localhost:8000/redoc
## テスト
- curl http://localhost:8000/
- curl -X GET http://localhost:8000/sample_get
- curl -X POST http://localhost:8000/sample_post
