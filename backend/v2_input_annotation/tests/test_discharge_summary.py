'''
#pip3 install pytest
#pip3 install httpx pytest-asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db
from app.main import app
from datetime import datetime

# --- テスト用DB（メモリ上SQLite） ---
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# --- get_db依存性を差し替え ---
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# --- サンプルデータ ---
sample_payload = {
    "karte_id": "K001",
    "registered_type": "MAIN",
    "registered_at": datetime.now().isoformat(),
    "registered_by": 1,
    "patient_name": "山田太郎",
    "patient_id": "P001",
}

@pytest.fixture(scope="module")
def created_id():
    """1件作成してIDを共有"""
    res = client.post("/discharge_summaries/", json=sample_payload)
    assert res.status_code == 200
    return res.json()["id"]

def test_read_all(created_id):
    res = client.get("/discharge_summaries/")
    assert res.status_code == 200
    data = res.json()
    assert any(d["id"] == created_id for d in data)

def test_read_one(created_id):
    res = client.get(f"/discharge_summaries/{created_id}")
    assert res.status_code == 200
    assert res.json()["karte_id"] == "K001"

def test_update(created_id):
    update_data = {"patient_name": "山田花子", "future_plan": "退院後フォローアップ外来"}
    res = client.put(f"/discharge_summaries/{created_id}", json=update_data)
    assert res.status_code == 200
    assert res.json()["patient_name"] == "山田花子"

def test_delete(created_id):
    res = client.delete(f"/discharge_summaries/{created_id}")
    assert res.status_code == 200
    assert "Deleted" in res.json()["message"]
'''