from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db, engine
from db.entities import user_account
from cruds import user_account_crud
from schemas import user_account_schema

router = APIRouter()

@router.get("/user_accounts", response_model=list[user_account_schema.UserAccount])
def read_accounts(db: Session = Depends(get_db)):
    return user_account_crud.get_all_accounts(db)

@router.get("/user_accounts/{account_id}", response_model=user_account_schema.UserAccount)
def read_account(account_id: int, db: Session = Depends(get_db)):
    account = user_account_crud.get_account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.post("/user_accounts", response_model=user_account_schema.UserAccount)
def create_account(account: user_account_schema.UserAccountCreate, db: Session = Depends(get_db)):
    return user_account_crud.create_account(db, account)

@router.put("/user_accounts/{account_id}", response_model=user_account_schema.UserAccount)
def update_account(account_id: int, account: user_account_schema.UserAccountUpdate, db: Session = Depends(get_db)):
    updated = user_account_crud.update_account(db, account_id, account)
    if not updated:
        raise HTTPException(status_code=404, detail="Account not found")
    return updated

@router.delete("/user_accounts/{account_id}")
def delete_account(account_id: int, db: Session = Depends(get_db)):
    deleted = user_account_crud.delete_account(db, account_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"message": "User account deleted"}
