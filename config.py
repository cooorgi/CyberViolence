class Config:
    db_username = "root"        # 数据库用户名
    db_password = "new123"      # 数据库密码
    db_host = "192.168.234.130" # 数据库地址
    db_port = 3306              # 数据库端口
    db_name = "vioana"          # 数据库名
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your_secret_key"

    LOGGING_ENABLED = True  # 设置为 False 可以禁用日志记录
