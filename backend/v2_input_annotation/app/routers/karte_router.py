from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas import karte_schema
from app.cruds import karte_crud

router = APIRouter(prefix="/kartes", tags=["kartes"])

@router.post("/", response_model=karte_schema.KarteResponse)
def create_karte(summary: karte_schema.KarteCreate,db: Session = Depends(get_db)):
    """新規登録"""
    return karte_crud.create_karte(db, summary)

@router.get("/{id}", response_model=karte_schema.KarteResponse)
def read_karte(id: int, db: Session = Depends(get_db)):
    """IDで1件取得"""
    db_data = karte_crud.get_karte(db, id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Karte not found")
    return db_data

@router.get("/", response_model=list[karte_schema.KarteResponse])
def read_kartes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """一覧取得"""
    return karte_crud.get_kartes(db, skip=skip, limit=limit)

@router.put("/{id}", response_model=karte_schema.KarteResponse)
def update_karte(id: int,model_update: karte_schema.KarteUpdate,db: Session = Depends(get_db)):
    """更新"""
    updated = karte_crud.update_karte(db, id, model_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Karte not found")
    return updated

@router.delete("/{id}")
def delete_karte(id: int, db: Session = Depends(get_db)):
    """削除"""
    deleted = karte_crud.delete_karte(db, id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Karte not found")
    return {"message": f"Karte {id} deleted successfully"}
