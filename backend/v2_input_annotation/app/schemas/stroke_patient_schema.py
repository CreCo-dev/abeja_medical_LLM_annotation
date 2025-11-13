"""
脳卒中患者(StrokePatient) に関する Pydantic スキーマ定義。

SQLAlchemy モデルから自動生成したベーススキーマを利用し、
用途（新規作成・更新・レスポンス）ごとに派生スキーマを定義する。
"""
from pydantic import BaseModel, create_model
from typing import Any, Optional
from datetime import datetime

from app.db.entities.stroke_patient import StrokePatient
from app.utils.database.schema import sqlalchemy_to_pydantic_v2

# 基本スキーマ（SQLAlchemyモデルから自動生成）
# カラム構造に基づき、自動的に型付きのPydanticモデルを作成。
# "id" フィールドは除外(DB側で自動採番号)。
StrokePatientBase = sqlalchemy_to_pydantic_v2(StrokePatient)

# 新規作成用スキーマ（POST用）
# DB上で nullable=False の項目のみ必須となる。
StrokePatientCreate = StrokePatientBase

# 更新用スキーマ（PUTリクエスト用）
# 全てのフィールドを Optional にしたバージョン。
StrokePatientUpdate = sqlalchemy_to_pydantic_v2(StrokePatient, all_optional=True)

# レスポンス用スキーマ（GETレスポンス用）
# DBから返す際に "id" など追加フィールドを含めたい場合に継承して拡張。
# model_config["from_attributes"]=True で ORMモード有効化。
class StrokePatientResponse(StrokePatientBase):
    id: int
    model_config = {"from_attributes": True}

