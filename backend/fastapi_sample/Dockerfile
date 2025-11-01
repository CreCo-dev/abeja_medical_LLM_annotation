# ベースイメージの指定
FROM python:3.12-slim

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    vim less \
    && rm -rf /var/lib/apt/lists/*

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# アプリケーションのコピー
COPY . /app

# 作業ディレクトリの設定
WORKDIR /app

# コマンドの指定
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
