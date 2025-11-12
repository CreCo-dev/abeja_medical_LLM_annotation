from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas import discharge_summary_schema
from app.cruds import discharge_summary_crud

router = APIRouter(prefix="/discharge_summaries", tags=["DischargeSummaries"])


@router.post("/", response_model=discharge_summary_schema.DischargeSummaryResponse)
def create_discharge_summary(summary: discharge_summary_schema.DischargeSummaryCreate,db: Session = Depends(get_db)):
    """新規登録"""
    return discharge_summary_crud.create_discharge_summary(db, summary)


@router.get("/{id}", response_model=discharge_summary_schema.DischargeSummaryResponse)
def read_discharge_summary(id: int, db: Session = Depends(get_db)):
    """IDで1件取得"""
    db_data = discharge_summary_crud.get_discharge_summary(db, id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Discharge summary not found")
    return db_data


@router.get("/", response_model=list[discharge_summary_schema.DischargeSummaryResponse])
def read_discharge_summaries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """一覧取得"""
    return discharge_summary_crud.get_discharge_summaries(db, skip=skip, limit=limit)


@router.put("/{id}", response_model=discharge_summary_schema.DischargeSummaryResponse)
def update_discharge_summary(id: int,model_update: discharge_summary_schema.DischargeSummaryUpdate,db: Session = Depends(get_db)):
    """更新"""
    updated = discharge_summary_crud.update_discharge_summary(db, id, model_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Discharge summary not found")
    return updated


@router.delete("/{id}")
def delete_discharge_summary(id: int, db: Session = Depends(get_db)):
    """削除"""
    deleted = discharge_summary_crud.delete_discharge_summary(db, id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Discharge summary not found")
    return {"message": f"Discharge summary {id} deleted successfully"}
