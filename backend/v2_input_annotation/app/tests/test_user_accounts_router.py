import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# テスト用データ定義
USER_PAYLOAD_1 = {"login_id": "1", "password": "11", "name": "Alice"}
USER_PAYLOAD_2 = {"login_id": "2", "password": "22", "name": "Bob"}
USER_EXPECTED_1 = {"id": 1, "login_id": "1", "name": "Alice"}
USER_EXPECTED_2 = {"id": 2, "login_id": "2", "name": "Bob"}

# POST /user_accounts/ : 新規登録
def test_create_user(client):
    """ユーザーを新規登録できることを確認"""
    response = client.post("/user_accounts/", json=USER_PAYLOAD_1)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == USER_EXPECTED_1

# GET /user_accounts/{id} : ユーザー1件取得
def test_read_user_by_id(client):
    """登録済みユーザーをIDで取得できることを確認"""
    client.post("/user_accounts/", json=USER_PAYLOAD_1)

    response = client.get("/user_accounts/1")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == USER_EXPECTED_1

# GET /user_accounts/ : 一覧取得
def test_read_user_list(client):
    """ユーザー一覧を取得できることを確認（順序非依存）"""
    # 前準備：2件登録
    client.post("/user_accounts/", json=USER_PAYLOAD_1)
    client.post("/user_accounts/", json=USER_PAYLOAD_2)

    response = client.get("/user_accounts/")
    assert response.status_code == status.HTTP_200_OK

    users = response.json()
    assert isinstance(users, list)
    assert len(users) == 2

    expected_users = [USER_EXPECTED_1, USER_EXPECTED_2]
    assert sorted(users, key=lambda u: u["id"]) == sorted(expected_users, key=lambda u: u["id"])

# PUT /user_accounts/{id} : 更新
def test_update_user(client):
    """ユーザー情報を更新できることを確認"""
    # 前準備：ユーザー登録
    client.post("/user_accounts/", json=USER_PAYLOAD_1)

    updated_payload = {"login_id": "2", "password": "22", "name": "Alice2"}
    expected_updated = {"id": 1, "login_id": "2", "name": "Alice2"}

    response = client.put("/user_accounts/1", json=updated_payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_updated

    # GETで更新結果を確認
    verify_response = client.get("/user_accounts/1")
    assert verify_response.status_code == status.HTTP_200_OK
    assert verify_response.json() == expected_updated


# DELETE /user_accounts/{id} : 削除
def test_delete_user(client):
    """ユーザーを削除できることを確認"""
    client.post("/user_accounts/", json=USER_PAYLOAD_1)

    response = client.delete("/user_accounts/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "User account 1 deleted successfully"}

    # 再取得で404を確認
    verify_response = client.get("/user_accounts/1")
    assert verify_response.status_code == status.HTTP_404_NOT_FOUND
    assert verify_response.json()["detail"] == "Account not found"
