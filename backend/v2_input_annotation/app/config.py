'''
.env

# =======================================
# 環境設定
# =======================================
APP_ENV=development

# =======================================
# CORS設定（Next.jsなどフロントエンドとの連携）
# ---------------------------------------
# 複数オリジンを許可する場合はカンマ区切りまたはJSON風リスト表記にします。
# 例: ["http://localhost:3000", "https://example.com"]
# =======================================
ALLOW_ORIGINS=["http://localhost:3000"]
ALLOW_METHODS=["*"]
ALLOW_HEADERS=["*"]
ALLOW_CREDENTIALS=True

# =======================================
# MySQL設定
# =======================================
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_DATABASE=sampledb

# =======================================
# JWT / セキュリティ設定
# =======================================
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256

'''
from pydantic_settings import BaseSettings
from functools import lru_cache
import os

# env から読み取る設定クラス（本番用）
class Settings(BaseSettings):
    
    app_env: str = "development"

    # CORS設定
    allow_origins: list[str]
    allow_methods: list[str]
    allow_headers: list[str]
    allow_credentials: bool = True

    # Database
    mysql_host: str
    mysql_port: int
    mysql_user: str
    mysql_password: str
    mysql_database: str

    # JWT / Security
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# コード直書き設定クラス（ローカル or Fallback用）
class Settings_on_code(BaseSettings):
    app_env: str = "local"

    # CORS設定
    allow_origins: list[str] = ["http://localhost:3000"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    allow_credentials: bool = True

    # Database
    mysql_host: str = "db"
    mysql_port: int = 3306
    mysql_user: str = "root"
    mysql_password: str = "password"
    mysql_database: str = "sampledb"

    # JWT / Security
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


# 共通アクセサ（どちらを使うか自動判定）
@lru_cache()
def get_settings():
    """
    優先順位：
      1. APP_ENV が 'production' → .env設定（Settings）
      2. それ以外（local, dev, test）→ コード直書き設定（Settings_on_code）
    """
    env = os.getenv("APP_ENV", "local").lower()

    if env in ("prod", "production"):
        print("[config] Using environment: .env Settings", flush=True)
        return Settings()  # .envから読み込む
    else:
        print("[config] Using environment: code Settings_on_code", flush=True)
        return Settings_on_code()
