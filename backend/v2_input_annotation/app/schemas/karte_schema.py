"""
カルテ(Karte) に関する Pydantic スキーマ定義。

SQLAlchemy モデルから自動生成したベーススキーマを利用し、
用途（新規作成・更新・レスポンス）ごとに派生スキーマを定義する。
"""
from pydantic import BaseModel, create_model
from typing import Any, Optional
from datetime import datetime

from app.db.entities.karte import Karte
from app.utils.database.schema import sqlalchemy_to_pydantic_v2

# 基本スキーマ（SQLAlchemyモデルから自動生成）
# カラム構造に基づき、自動的に型付きのPydanticモデルを作成。
# "id" フィールドは除外(DB側で自動採番号)。
KarteBase = sqlalchemy_to_pydantic_v2(Karte)

# 新規作成用スキーマ（POST用）
# DB上で nullable=False の項目のみ必須となる。
KarteCreate = KarteBase

# 更新用スキーマ（PUTリクエスト用）
# 全てのフィールドを Optional にしたバージョン。
KarteUpdate = sqlalchemy_to_pydantic_v2(Karte, all_optional=True)

# レスポンス用スキーマ（GETレスポンス用）
# DBから返す際に "id" など追加フィールドを含めたい場合に継承して拡張。
# model_config["from_attributes"]=True で ORMモード有効化。
class KarteResponse(KarteBase):
    id: int
    model_config = {"from_attributes": True}

