# Standard Library
import logging
import os
import inspect
from datetime import datetime, timedelta, timezone

# Third Party


# CustomFormatterクラスの定義
# このクラスは、ログメッセージのフォーマットをカスタマイズする
class CustomFormatter(logging.Formatter):
    def format(self, record):
        # 呼び出し元のファイル名と行番号をログメッセージに追加する
        frame = inspect.currentframe()
        outer_frames = inspect.getouterframes(frame)
        
        # loggingモジュールとlog_util.pyを呼び出しているフレームをスキップする
        app_frame_info = None
        for frame_info in outer_frames:
            if not frame_info.filename.endswith(('logging/__init__.py', 'log_config.py', 'output_log.py')):
                app_frame_info = frame_info
                break

        # 呼び出し元のファイル名と行番号を設定する
        if app_frame_info is not None:
            record.filename = os.path.basename(app_frame_info.filename)
            record.pathname = app_frame_info.filename
            record.lineno = app_frame_info.lineno
        else:
            record.filename = "<unknown>"
            record.pathname = "<unknown>"
            record.lineno = 0

        # 親クラスのformatメソッドを使用してログメッセージをフォーマットする
        return super().format(record)
    
    
    # ログ出力時刻を日本時間に変更
    def formatTime(self, record: logging.LogRecord, datefmt=None):
        datefmt = "%Y-%m-%d %H:%M:%S,%03d"
        tz_jst = timezone(timedelta(hours=+9), 'JST')
        created_time  = datetime.fromtimestamp(record.created, tz=tz_jst)
        time = created_time.strftime(datefmt)
        return time


# ロガーの設定関数
# 指定された名前のロガーを設定する
def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        # コンソールハンドラを設定する
        console_handler = logging.StreamHandler()
        formatter = CustomFormatter('[%(levelname)s]-[%(asctime)s]-[%(message)s]-[%(pathname)s:%(lineno)d]')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
