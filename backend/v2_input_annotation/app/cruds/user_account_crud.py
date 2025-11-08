from sqlalchemy.orm import Session
from db.entities import user_account
from schemas import user_account_schema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def get_all_accounts(db: Session):
    return db.query(user_account.UserAccount).all()

def get_account_by_id(db: Session, account_id: int):
    return db.query(user_account.UserAccount).filter(user_account.UserAccount.id == account_id).first()

def create_account(db: Session, account: user_account_schema.UserAccountCreate):
    #print(account.password)
    hashed_password = get_password_hash(account.password)
    #print(hashed_password)
    new_account = user_account.UserAccount(
        login_id=account.login_id,
        password=hashed_password,
        name=account.name
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def update_account(db: Session, account_id: int, account: user_account_schema.UserAccountUpdate):
    db_account = db.query(user_account.UserAccount).filter(user_account.UserAccount.id == account_id).first()
    if db_account:
        db_account.login_id = account.login_id
        db_account.password = get_password_hash(account.password)
        db_account.name = account.name
        db.commit()
        db.refresh(db_account)
    return db_account

def delete_account(db: Session, account_id: int):
    db_account = db.query(user_account.UserAccount).filter(user_account.UserAccount.id == account_id).first()
    if db_account:
        db.delete(db_account)
        db.commit()
    return db_account
