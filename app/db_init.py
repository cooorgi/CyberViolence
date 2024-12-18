import os

from sqlalchemy import event, Engine

from app.extensions import db


# 设置连接时字符集为 utf8mb4
@event.listens_for(Engine, "connect")
def set_utf8mb4_encoding(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("SET NAMES 'utf8mb4'")
    cursor.close()

def execute_sql_files(app):
    """在应用上下文中执行SQL初始化脚本"""
    sql_files = [
        "sql/vioana.sql",
    ]

    base_path = os.path.dirname(os.path.abspath(__file__))
    for sql_file in sql_files:
        filepath = os.path.join(base_path, "..", sql_file)  # 相对路径
        if os.path.exists(filepath):
            app.logger.info(f"Executing {sql_file}...")
            try:
                with open(filepath, 'r', encoding='utf8mb4') as file:
                    sql_statements = file.read()
                with app.app_context():
                    with db.engine.connect() as connection:
                        for statement in sql_statements.split(';'):
                            if statement.strip():
                                connection.execute(statement)
            except Exception as e:
                app.logger.error(f"Error executing {sql_file}: {e}")
        else:
            app.logger.warning(f"File {sql_file} not found.")
