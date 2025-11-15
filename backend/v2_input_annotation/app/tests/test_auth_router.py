# app/tests/test_auth_router.py
from fastapi import status
from fastapi.testclient import TestClient
from jose import jwt

from app.main import app
from app.config import get_settings

settings = get_settings()
client = TestClient(app)

# ============================================================
# テスト用ユーザー
# ============================================================

USER_PAYLOAD = {"login_id": "loginuser", "password": "secret", "name": "Alice"}
USER_EXPECTED = {"id": 1, "login_id": "loginuser", "name": "Alice"}

# ============================================================
# /login : ログインしてトークンを取得
# ============================================================

def test_login_success(client):
    """正しいログイン情報でトークンが発行されることを確認"""
    # 前準備：ユーザー登録
    client.post("/user_accounts/", json=USER_PAYLOAD)

    # OAuth2PasswordRequestForm の仕様に従い、form-dataで送信
    login_data = {"username": USER_PAYLOAD["login_id"], "password": USER_PAYLOAD["password"]}
    response = client.post("/login", data=login_data)

    assert response.status_code == status.HTTP_200_OK

    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"

    # トークンをデコードして "sub" に login_id が含まれていることを確認
    payload = jwt.decode(token_data["access_token"], settings.secret_key, algorithms=[settings.algorithm])
    assert payload["sub"] == USER_PAYLOAD["login_id"]


def test_login_invalid_password(client):
    """パスワードが間違っている場合は401エラーとなることを確認"""
    # 前準備：ユーザー登録
    client.post("/user_accounts/", json=USER_PAYLOAD)

    invalid_data = {"username": USER_PAYLOAD["login_id"], "password": "wrongpass"}
    response = client.post("/login", data=invalid_data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Invalid credentials"


def test_read_own_account(client):
    """有効なトークンで自分のユーザー情報が取得できることを確認"""
    # 前準備：ユーザー登録 + ログイン
    client.post("/user_accounts/", json=USER_PAYLOAD)
    login_data = {"username": USER_PAYLOAD["login_id"], "password": USER_PAYLOAD["password"]}
    login_response = client.post("/login", data=login_data)
    token = login_response.json()["access_token"]

    # Authorization ヘッダー付きで /me にアクセス
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user_accounts_with_auth/me", headers=headers)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == USER_EXPECTED

def test_read_own_account_invalid_token(client):
    """無効トークンでは401エラーとなることを確認"""
    headers = {"Authorization": "Bearer invalid.token.value"}
    response = client.get("/user_accounts_with_auth/me", headers=headers)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Invalid or expired token"
