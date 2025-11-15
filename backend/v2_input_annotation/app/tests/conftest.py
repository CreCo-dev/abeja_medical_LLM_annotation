import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import Base, get_db

TEST_DB_PATH = "./test.db"
SQLALCHEMY_TEST_URL = f"sqlite:///{TEST_DB_PATH}"

engine = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def cleanup_test_db():
    """pytest 全体の実行後に test.db を削除する"""
    yield
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
        print("\n[TEST CLEANUP] test.db removed.")


@pytest.fixture(scope="function")
def db_session():
    """テスト毎にDB初期化"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(db_session):
    from fastapi.testclient import TestClient
    from app.main import app

    def override_get_db():
        try:
            yield db_session
        finally:
            pass  # closeは db_session に任せる
    
    app.dependency_overrides[get_db] = override_get_db

    # TestClient は return で返すのが自然
    return TestClient(app)
