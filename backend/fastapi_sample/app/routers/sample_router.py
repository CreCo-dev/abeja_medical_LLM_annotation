
import os


from sqlalchemy import create_engine, text

# Third Party
from fastapi import APIRouter


from utils.logger.log_config import setup_logger
from utils.logger.output_log import log_message


router = APIRouter()

# ロガーの設定---------------------------------------
logger = setup_logger(__name__)
# ---------------------------------------------------


@router.get("/sample_get")  #, response_model=Zzz
async def sample_get():
    #log_message(logger, "D0002", [f"{sample_get} start"])

    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@db:3306/sampledb")

    engine = create_engine(DATABASE_URL, echo=True, future=True)

    # 例: 接続確認
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ MySQL connected:", result.scalar())
            log_message(logger, "D0001", ["MySQL connected"])
    except Exception as e:
        print("❌ DB connection failed:", e)
        log_message(logger, "D0001", ["DB connection failed"])


    return "ok router get"


@router.post("/sample_post")  #, response_model=Zzz
async def sample_post():
    log_message(logger, "D0002", [f"{sample_post} start"])
    return {"message": "ok router post"}
