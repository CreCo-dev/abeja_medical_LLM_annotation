from pydantic import BaseModel, create_model
from app.db.entities.discharge_summary import DischargeSummary
from typing import Any, Optional
from datetime import datetime

def sqlalchemy_to_pydantic_v2(model, *, all_optional: bool = False):
    """SQLAlchemyモデル → Pydanticモデルを自動生成 (v2対応)
       all_optional=True の場合、全てのフィールドを Optional にする
    """
    from typing import Any, Optional

    fields = {}
    for name, column in model.__table__.columns.items():
        if name == "id":  # ← IDを除外
            continue

        # SQLAlchemyの型からPython型を推定
        try:
            py_type = column.type.python_type
        except NotImplementedError:
            py_type = Any

        # all_optional=TrueならすべてOptional
        if all_optional:
            field_type = Optional[py_type]
            default = None
        else:
            # 通常モード：nullableやdefaultでOptional判定
            if column.nullable or column.default is not None:
                field_type = Optional[py_type]
                default = None
            else:
                field_type = py_type
                default = ...

        fields[name] = (field_type, default)

    model_name = model.__name__ + ("Update" if all_optional else "Schema")
    return create_model(model_name, **fields)

# --- Create/Update/Response モデル定義 ---
DischargeSummaryBase = sqlalchemy_to_pydantic_v2(DischargeSummary)
DischargeSummaryCreate = DischargeSummaryBase
DischargeSummaryUpdate = sqlalchemy_to_pydantic_v2(DischargeSummary, all_optional=True)
class DischargeSummaryResponse(DischargeSummaryBase):
    id: int
    model_config = {"from_attributes": True}


from typing import Type
from pydantic import BaseModel


