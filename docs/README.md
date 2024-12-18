
```angular2html
bigdata/
├── app/
│   ├── __init__.py                         # 初始化 Flask 应用
│   ├── extensions.py                       # 扩展库初始化
│   ├── db_init.py                          # 初始化数据库
│   ├── models/                             # 数据库模型文件夹
│   │   ├── __init__.py                     # 模型初始化
│   │   ├── xhs.py                          # 小红书模型
│   │   ├── zhihu.py                        # 知乎模型
│   │   ├── bili.py                         # B站模型
│   ├── routes/                             # 路由文件夹
│   │   ├── __init__.py                     # 路由初始化
│   │   ├── xhs.py                          # 小红书接口路由
│   │   ├── zhihu.py                        # 知乎接口路由
│   │   ├── bilibili.py                     # B站接口路由
│   ├── templates/             
│   │   ├── index.html                      # 可视化大屏
│   ├── static/                             # 前端
│   │   ├── css/                            
│   │   ├── font/                        
│   │   ├── images/                     
│   │   ├── js/                 
├── sql/                                    # sql脚本文件夹
│   ├── vioana.sql
├── docs/                                   # 说明文件夹
│   ├── README.md                           # 项目结构
│   ├── api.md                              # 接口文档
├── log/                                    # 日志文件夹
├── config.py                               # 配置文件
├── run.py                                  # 项目启动文件
├── requirements.txt                        # 项目依赖
```

