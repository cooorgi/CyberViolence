from flask import Flask
from app.extensions import db, init_log, log
from app.db_init import execute_sql_files

def create_app(init_db=False):
    app = Flask(__name__)

    # 加载配置
    app.config.from_object('config.Config')

    # 初始化数据库
    db.init_app(app)

    # 配置日志系统
    init_log(app)

    # 初始化日志
    app.logger.info("Flask application initialized successfully.")

    # 注册请求日志记录钩子
    log(app)

    # 注册路由
    from app.routes import register_routes
    register_routes(app)

    # 如果需要初始化数据库，则执行SQL脚本
    if init_db:
        execute_sql_files(app)

    return app
