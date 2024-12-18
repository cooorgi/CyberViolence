from app.extensions import db
from app.models.xhs import xhsNoteComment
from app.models.zhihu import zhihuContent, zhihuComment
from app.models.bili import bilibiliVideoComment, bilibiliVideo

def init_models(app):
    with app.app_context():
        db.create_all()

