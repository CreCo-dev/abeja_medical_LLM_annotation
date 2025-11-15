from sqlalchemy.orm import Session
from app.db.entities import user_account
from app.db.entities.user_account import UserAccount
from app.schemas import user_account_schema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserAccount).offset(skip).limit(limit).all()


def get_account_by_id(db: Session, id: int):
    return db.query(UserAccount).filter(UserAccount.id == id).first()

def create_account(db: Session, account: user_account_schema.UserAccountCreate):
    #print(account.password)
    hashed_password = get_password_hash(account.password)
    #print(hashed_password)
    new_account = UserAccount(
        login_id=account.login_id,
        password=hashed_password,
        name=account.name
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def update_account(db: Session, id: int, account: user_account_schema.UserAccountUpdate):
    db_account = db.query(UserAccount).filter(UserAccount.id == id).first()
    if db_account:
        db_account.login_id = account.login_id
        db_account.password = get_password_hash(account.password)
        db_account.name = account.name
        db.commit()
        db.refresh(db_account)
    return db_account

def delete_account(db: Session, id: int):
    db_account = db.query(UserAccount).filter(UserAccount.id == id).first()
    if db_account:
        db.delete(db_account)
        db.commit()
    return db_account
