from app.extensions import db
from app.models.base import BaseModel


class zhihuContent(BaseModel):
    __tablename__ = 'washed_zhihu_content'              # 知乎帖子

    content_type = db.Column(db.String(255))            # 帖子类型
    content_text = db.Column(db.String(255))            # 帖子内容
    title = db.Column(db.String(255))                   # 帖子标题
    desc = db.Column(db.String(255))                    # 简介


class zhihuComment(BaseModel):
    __tablename__ = 'washed_zhihu_comment'              # 知乎帖子评论

    content = db.Column(db.String(255))                 # 评论内容
    ip_location = db.Column(db.String(255))             # IP地址
    dislike_count = db.Column(db.Integer)               # 反对数
    content_type = db.Column(db.String(255))            # 评论类型
    attitude = db.Column(db.String(100))                # 情感分析：正向or负向


