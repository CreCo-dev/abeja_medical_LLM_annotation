from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas import user_account_schema
from app.cruds import user_account_crud


router = APIRouter(prefix="/user_accounts", tags=["user_accounts"])

@router.post("/", response_model=user_account_schema.UserAccount)
def create_account(account: user_account_schema.UserAccountCreate, db: Session = Depends(get_db)):
    """新規登録"""
    return user_account_crud.create_account(db, account)

@router.get("/{id}", response_model=user_account_schema.UserAccount)
def read_account(id: int, db: Session = Depends(get_db)):
    """IDで1件取得"""
    account = user_account_crud.get_account_by_id(db, id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.get("/", response_model=list[user_account_schema.UserAccount])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """一覧取得"""
    return user_account_crud.get_accounts(db, skip=skip, limit=limit)

@router.put("/{id}", response_model=user_account_schema.UserAccount)
def update_account(id: int, account: user_account_schema.UserAccountUpdate, db: Session = Depends(get_db)):
    """更新"""
    updated = user_account_crud.update_account(db, id, account)
    if updated is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return updated

@router.delete("/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    """削除"""
    deleted = user_account_crud.delete_account(db, id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"message": f"User account {id} deleted successfully"}
