import argparse
from app import create_app
from app.db_init import execute_sql_files  # 导入SQL初始化逻辑

def main():
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description="Flask Application Controller")
    parser.add_argument(
        "--db", action="store_true", help="Initialize the database with SQL scripts."
    )
    parser.add_argument(
        "--port", type=int, default=5000, help="Port to run the Flask application on."
    )
    args = parser.parse_args()

    # 创建 Flask 应用
    app = create_app()

    # 根据参数执行初始化数据库逻辑
    if args.db:
        print("Initializing database...")
        execute_sql_files(app)
        print("Database initialized successfully.")
    else:
        # 启动 Flask 服务，指定端口
        print(f"Starting Flask app on port {args.port}...")
        app.run(debug=True, port=args.port)  # 启动服务并指run定端口

if __name__ == "__main__":
    main()
