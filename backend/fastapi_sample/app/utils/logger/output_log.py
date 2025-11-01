# Standard Library
import traceback

# Module
from utils.logger.log_message import (
    LOG_MESSAGES
)

# ログメッセージを出力する関数
# 指定されたログレベルに応じて適切なログメッセージを出力する
def log_message(logger, message_code: str, message_items: list = []):
    
    if logger == None:
        return
    
    # メッセージコードに紐づくメッセージ取得
    if len(message_items) == 0:
        message = LOG_MESSAGES.get(message_code, "")
    else:
        message_format = LOG_MESSAGES.get(message_code, "")
        # if message_format == "":
        #     return
        
        message = message_format.format(message_items)
    
    # メッセージコードのログレベルに応じてログ出力
    log_level = message_code[0]
    # DEBUGログ
    if log_level == 'D':
        logger.debug(message)

    # INFOログ
    elif log_level == 'I':
        logger.info(message)

    # WARNINGログ
    elif log_level == 'W':
        logger.warning(message)

    # ERRORログ
    elif log_level == 'E':
        logger.error(message, exc_info=True)
