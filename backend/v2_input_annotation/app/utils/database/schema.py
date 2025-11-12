"""
sqlalchemy_to_pydantic.py

SQLAlchemy モデルから Pydantic モデルを自動生成するユーティリティ。
FastAPI v2 対応版。
"""

from typing import Any, Optional
from pydantic import create_model


def sqlalchemy_to_pydantic_v2(model, *, all_optional: bool = False):
    """
    SQLAlchemyモデル → Pydanticモデルを自動生成 (v2対応)
    
    Args:
        model: SQLAlchemy モデルクラス
        all_optional (bool): True の場合、全てのフィールドを Optional にする (更新用スキーマなどに使用)

    Returns:
        pydantic.BaseModel サブクラス
    """
    fields = {}

    for name, column in model.__table__.columns.items():
        if name == "id":  # IDは除外
            continue

        # SQLAlchemy の型から Python 型を推定
        try:
            py_type = column.type.python_type
        except NotImplementedError:
            py_type = Any

        # all_optional=True の場合、全フィールド Optional
        if all_optional:
            field_type = Optional[py_type]
            default = None
        else:
            # 通常モード: nullable や default により Optional 判定
            if column.nullable or column.default is not None:
                field_type = Optional[py_type]
                default = None
            else:
                field_type = py_type
                default = ...

        fields[name] = (field_type, default)

    model_name = model.__name__ + ("Update" if all_optional else "Schema")
    return create_model(model_name, **fields)
