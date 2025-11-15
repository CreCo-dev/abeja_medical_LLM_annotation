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
DATABASE_URL=mysql+pymysql://root:password@db:3306/sampledb

# =======================================
# JWT / セキュリティ設定
# =======================================
SECRET_KEY=dev-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

'''
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from functools import lru_cache
import os

# Baseクラス（型定義のみ共通）
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

# 本番設定（.envから読み取る）
class ProdSettings(CommonSettings):
    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache()
def get_settings() -> CommonSettings:
    """
    APP_ENV が 'production' → .env設定を利用
    それ以外（local）         → コード直書き設定(ローカルでの動作確認用)
    """

    env = os.getenv("APP_ENV", "local").lower()

    if env in ("production"):
        print("[config] Using Production Settings (.env)", flush=True)
        return ProdSettings()

    print("[config] Using CommonSettings (environment or defaults)", flush=True)
    return CommonSettings()
