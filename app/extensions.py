import os
import logging
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask import request

db = SQLAlchemy()

# 日志开关标识 (可在 config.py 中配置)
LOGGING_ENABLED =  Config.LOGGING_ENABLED

def init_log(app):
    """初始化日志系统"""
    if LOGGING_ENABLED:
        log_dir = "log"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # 确保日志目录存在

        log_filename = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

        # 配置日志格式
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # 文件日志处理器
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.INFO)

        # 控制台日志处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        console_handler.setLevel(logging.INFO)

        # 添加处理器到 Flask 日志系统
        app.logger.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.addHandler(console_handler)


def log(app):
    """请求后记录日志"""
    if LOGGING_ENABLED:
        @app.after_request
        def log_response(response):
            app.logger.info(
                f"{request.remote_addr} - {request.method} {request.path} "
                f"Status: {response.status_code} - User-Agent: {request.user_agent}"
            )
            return response