import pytest
from fastapi import status
from fastapi.testclient import TestClient
from datetime import datetime, timezone

from app.main import app

client = TestClient(app)

# テスト用データ定義
USER_PAYLOAD = {"login_id": "1", "password": "11", "name": "Alice"}
KARTE_PAYLOAD = {"karte_data_id": "123","karte_name": "カルテ123","data_type": "DC"}
DS_PAYLOAD = {
  "karte_id": 1,
  "registered_type": "LLM",
  "registered_at": "2025-11-15T16:18:49.301Z",
  "registered_by": 1,
  "patient_name": "患者1",
  "patient_id": "1"}

def test_create_discharge_summary(client):
    """新規登録できることを確認"""

    response = client.post("/user_accounts/", json=USER_PAYLOAD)
    response = client.post("/kartes/", json=KARTE_PAYLOAD)

    response = client.post("/discharge_summaries/", json=DS_PAYLOAD)

    assert response.status_code == status.HTTP_200_OK
    ds = response.json()

    assert ds["id"] == 1
    assert ds["karte_id"] == DS_PAYLOAD["karte_id"]
    assert ds["registered_type"] == DS_PAYLOAD["registered_type"]
    #assert ds["registered_at"] == DS_PAYLOAD["registered_at"]
    expected = datetime.fromisoformat(DS_PAYLOAD["registered_at"].replace("Z", "+00:00")).replace(tzinfo=None)
    actual = datetime.fromisoformat(ds["registered_at"])
    assert actual == expected
    assert ds["registered_by"] == DS_PAYLOAD["registered_by"]
    assert ds["registered_type"] == DS_PAYLOAD["registered_type"]
    assert ds["patient_name"] == DS_PAYLOAD["patient_name"]
    assert ds["patient_id"] == DS_PAYLOAD["patient_id"]

def test_read_discharge_summary_by_id(client):
    """登録済みの情報をIDで取得できることを確認"""
    response = client.post("/user_accounts/", json=USER_PAYLOAD)
    response = client.post("/kartes/", json=KARTE_PAYLOAD)

    response = client.post("/discharge_summaries/", json=DS_PAYLOAD)

    response = client.get("/discharge_summaries/1")

    assert response.status_code == status.HTTP_200_OK
    ds = response.json()

    assert ds["id"] == 1
    assert ds["karte_id"] == DS_PAYLOAD["karte_id"]
    assert ds["registered_type"] == DS_PAYLOAD["registered_type"]
    #assert ds["registered_at"] == DS_PAYLOAD["registered_at"]
    expected = datetime.fromisoformat(DS_PAYLOAD["registered_at"].replace("Z", "+00:00")).replace(tzinfo=None)
    actual = datetime.fromisoformat(ds["registered_at"])
    assert actual == expected
    assert ds["registered_by"] == DS_PAYLOAD["registered_by"]
    assert ds["registered_type"] == DS_PAYLOAD["registered_type"]
    assert ds["patient_name"] == DS_PAYLOAD["patient_name"]
    assert ds["patient_id"] == DS_PAYLOAD["patient_id"]
