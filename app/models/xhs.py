from app.extensions import db
from app.models.base import BaseModel


class xhsNoteComment(BaseModel):
    __tablename__ = 'washed_xhs_note_comment'       # 小红书帖子评论

    ip_location =db.Column(db.String(255))          # IP地址
    content = db.Column(db.String(255))             # 评论内容
    attitude = db.Column(db.String(100))            # 情感分析：正向or负向

class xhsNote(BaseModel):
    __tablename__ = 'washed_xhs_note'               # 小红书帖子

    ip_location = db.Column(db.String(255))         # IP地址
    type = db.Column(db.String(255))                # 帖子类型
    title = db.Column(db.String(255))               # 标题
    desc = db.Column(db.String(255))                # 简介
    collected_count = db.Column(db.Integer)         # 收藏数
    share_count = db.Column(db.Integer)             # 分享数
    tag_list = db.Column(db.String(255))            # 分类标签
    platform = db.Column(db.String(255))            # 来源

