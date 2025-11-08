# app/routers/auth_router.py

from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from db.database import get_db
from db.entities.user_account import UserAccount
from config import get_settings
from schemas.auth_schema import TokenResponse

router = APIRouter()
settings = get_settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# ==========================================================
# JWT関連ユーティリティ
# ==========================================================
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def decode_access_token(token: str):
    try:
        #print({'decode_access_token()', token}, flush=True)
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload.get("sub")
    except JWTError:
        #print({'decode_access_token()  JWTError',JWTError}, flush=True)
        return None

# ==========================================================
# 認証API
# ==========================================================
@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    ログインID(login_id)とパスワードを受け取り、JWTを返す
    """
    user = db.query(UserAccount).filter(UserAccount.login_id == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    token = create_access_token({"sub": user.login_id}, token_expires)
    return {"access_token": token, "token_type": "bearer"}



@router.get("/user_accounts_with_auth/me")
def read_own_account(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """ログイン中ユーザーの情報取得"""
    #print({'token',token})
    login_id = decode_access_token(token)
    #print({'login_id',login_id})
    if not login_id:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.query(UserAccount).filter(UserAccount.login_id == login_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": user.id, "login_id": user.login_id, "name": user.name}
