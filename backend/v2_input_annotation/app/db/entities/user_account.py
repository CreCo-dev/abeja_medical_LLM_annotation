from sqlalchemy import Column, Integer, String
from db.database import Base
from db.database import engine

class UserAccount(Base):
    __tablename__ = "user_accounts"

    id = Column(Integer, primary_key=True, index=True)
    login_id = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(50), nullable=False)

Base.metadata.create_all(bind=engine)
print("[DB INIT] user_accounts created.", flush=True)