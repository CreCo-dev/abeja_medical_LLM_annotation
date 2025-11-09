import sys
import os 
# このファイルの親ディレクトリ（＝プロジェクトルート）をパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

'''

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import Base
from app.config import get_settings

# ✅ モデルを明示的に import（__init__.py がなくてもOK）
import app.db.entities.user_account
import app.db.entities.karte
import app.db.entities.stroke_patient
import app.db.entities.discharge_summary


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """pytest 実行時のテストDBを初期化"""
    settings = get_settings()
    db_url = settings.database_url or "sqlite:////tmp/test.db"

    print(f"[TEST INIT] Using DB: {db_url}", flush=True)

    engine = create_engine(
        db_url,
        connect_args={"check_same_thread": False},
        echo=True,  # SQLログ表示
    )

    print("[TEST INIT] Creating tables...", flush=True)
    Base.metadata.create_all(bind=engine)
    print("[TEST INIT] Tables created successfully.", flush=True)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # ✅ get_dbを差し替え
    def _override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    import app.db.database
    app.db.database.engine = engine
    app.db.database.SessionLocal = TestingSessionLocal
    app.db.database.get_db = _override_get_db

    yield

    print("[TEST CLEANUP] Dropping tables...", flush=True)
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("/tmp/test.db"):
        os.remove("/tmp/test.db")
'''