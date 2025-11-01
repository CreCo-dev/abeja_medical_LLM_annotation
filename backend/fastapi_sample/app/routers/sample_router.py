

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
    log_message(logger, "D0002", [f"{sample_get} start"])
    return "ok router get"


@router.post("/sample_post")  #, response_model=Zzz
async def sample_post():
    log_message(logger, "D0002", [f"{sample_post} start"])
    return {"message": "ok router post"}
