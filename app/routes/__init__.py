from flask import Blueprint, render_template
from app.routes.xhs import xhs
from app.routes.zhihu import zhihu
from app.routes.bili import bili
from flask_cors import CORS


index = Blueprint('index', __name__)
CORS(index)  # 启用 CORS 允许所有路由

@index.route('/')
def home():
    return render_template('index.html')
def register_routes(app):
    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(xhs, url_prefix='/xhs')
    app.register_blueprint(zhihu, url_prefix='/zhihu')
    app.register_blueprint(bili, url_prefix='/bilibili')
