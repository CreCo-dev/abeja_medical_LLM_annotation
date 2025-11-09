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
DATABASE_URL=mysql+pymysql://root:password@db:3306/sampledb

# =======================================
# JWT / セキュリティ設定
# =======================================
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256

'''
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from functools import lru_cache
import os


# =====================================
# Baseクラス（型定義のみ共通）
# =====================================
class CommonSettings(BaseSettings):
    app_env: str
    allow_origins: list[str]
    allow_methods: list[str]
    allow_headers: list[str]
    allow_credentials: bool
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


# =====================================
# 本番設定（.envから読み取る）
# =====================================
class ProdSettings(CommonSettings):
    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")

# =====================================
# 開発環境（オンコード定義）
# =====================================
class LocalSettings(CommonSettings):
    app_env: str = "local"

    allow_origins: list[str] = ["http://localhost:3000"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    allow_credentials: bool = True

    database_url: str = "mysql+pymysql://root:password@db:3306/sampledb"

    secret_key: str = "dev-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


# =====================================
# テスト環境（オンコード定義）
# =====================================
class TestSettings(CommonSettings):
    app_env: str = "test"

    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    allow_credentials: bool = True

    # SQLite（メモリ）を使用してテストDBを独立化
    database_url: str = "sqlite:////tmp/test.db"

    secret_key: str = "test-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


# =====================================
# 環境切り替えロジック
# =====================================
@lru_cache()
def get_settings() -> CommonSettings:
    """
    優先順位：
      1. APP_ENV が 'production' → .env設定（Settings）
      2. それ以外（local, dev, test）→ コード直書き設定（SettingsOnCode）
    """
    env = os.getenv("APP_ENV", "local").lower()

    if env in ("prod", "production"):
        print("[config] Using Production Settings (.env)", flush=True)
        return ProdSettings()

    elif env in ("test", "testing", "pytest"):
        print("[config] Using Test Settings (on-code)", flush=True)
        return TestSettings()

    else:
        print("[config] Using Local Settings (on-code)", flush=True)
        return LocalSettings()
