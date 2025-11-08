from sqlalchemy.orm import Session
from db import models
from schemas import user_account_schema

def get_all_accounts(db: Session):
    return db.query(models.UserAccount).all()

def get_account_by_id(db: Session, account_id: int):
    return db.query(models.UserAccount).filter(models.UserAccount.id == account_id).first()

def create_account(db: Session, account: user_account_schema.UserAccountCreate):
    new_account = models.UserAccount(
        login_id=account.login_id,
        password=account.password,  # ← 本来はハッシュ化推奨
        name=account.name
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def update_account(db: Session, account_id: int, account: user_account_schema.UserAccountUpdate):
    db_account = db.query(models.UserAccount).filter(models.UserAccount.id == account_id).first()
    if db_account:
        db_account.login_id = account.login_id
        db_account.password = account.password
        db_account.name = account.name
        db.commit()
        db.refresh(db_account)
    return db_account

def delete_account(db: Session, account_id: int):
    db_account = db.query(models.UserAccount).filter(models.UserAccount.id == account_id).first()
    if db_account:
        db.delete(db_account)
        db.commit()
    return db_account
