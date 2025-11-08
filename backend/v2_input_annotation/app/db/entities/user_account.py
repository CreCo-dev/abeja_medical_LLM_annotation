from sqlalchemy import Column, Integer, String
from db.database import Base, engine

# ユーザーアカウント
class UserAccount(Base):
    __tablename__ = "user_accounts"

    # ID
    id = Column(Integer, primary_key=True, index=True)
    # ログインID
    login_id = Column(String(50), unique=True, nullable=False)
    # パスワード
    password = Column(String(255), nullable=False)
    # 名前
    name = Column(String(50), nullable=False)

Base.metadata.create_all(bind=engine)
print("[DB INIT] user_accounts created.", flush=True)