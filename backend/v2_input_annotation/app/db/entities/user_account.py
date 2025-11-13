from sqlalchemy import Column, Integer, String
from app.db.database import Base, engine


# ユーザーアカウント
class UserAccount(Base):
    __tablename__ = "user_accounts"
    __table_args__ = {"info": {"ja_name": "ユーザーアカウント"}}

    # ID
    id = Column(Integer, primary_key=True, index=True, info={"ja_name": "ID"})
    # ログインID
    login_id = Column(String(50), unique=True, nullable=False, info={"ja_name": "ログインID"})
    # パスワード
    password = Column(String(255), nullable=False, info={"ja_name": "パスワード"})
    # 名前
    name = Column(String(50), nullable=False, info={"ja_name": "名前"})


Base.metadata.create_all(bind=engine)
print("[DB INIT] user_accounts created.", flush=True)
