from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas import stroke_patient_schema
from app.cruds import stroke_patient_crud

router = APIRouter(prefix="/stroke_patients", tags=["stroke_patients"])

@router.post("/", response_model=stroke_patient_schema.StrokePatientResponse)
def create_stroke_patient(summary: stroke_patient_schema.StrokePatientCreate,db: Session = Depends(get_db)):
    """新規登録"""
    return stroke_patient_crud.create_stroke_patient(db, summary)

@router.get("/{id}", response_model=stroke_patient_schema.StrokePatientResponse)
def read_stroke_patient(id: int, db: Session = Depends(get_db)):
    """IDで1件取得"""
    db_data = stroke_patient_crud.get_stroke_patient(db, id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="StrokePatient not found")
    return db_data

@router.get("/", response_model=list[stroke_patient_schema.StrokePatientResponse])
def read_stroke_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """一覧取得"""
    return stroke_patient_crud.get_stroke_patients(db, skip=skip, limit=limit)

@router.put("/{id}", response_model=stroke_patient_schema.StrokePatientResponse)
def update_stroke_patient(id: int,model_update: stroke_patient_schema.StrokePatientUpdate,db: Session = Depends(get_db)):
    """更新"""
    updated = stroke_patient_crud.update_stroke_patient(db, id, model_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="StrokePatient not found")
    return updated

@router.delete("/{id}")
def delete_stroke_patient(id: int, db: Session = Depends(get_db)):
    """削除"""
    deleted = stroke_patient_crud.delete_stroke_patient(db, id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="StrokePatient not found")
    return {"message": f"StrokePatient {id} deleted successfully"}
