from app.extensions import db
from app.models.base import BaseModel


class bilibiliVideo(BaseModel):
    __tablename__ = 'washed_bilibili_video'             # 清洗完的bilibili视频/帖子

    title = db.Column(db.String(255))                   # 标题
    desc = db.Column(db.String(255))                    # 简介
    video_play_count = db.Column(db.Integer)            # 播放数
    video_danmaku = db.Column(db.Integer)               # 弹幕数

class bilibiliVideoComment(BaseModel):
    __tablename__ = 'washed_bilibili_video_comment'     # 清洗完的bilibili视频/帖子评论

    content = db.Column(db.String(255))                 # 评论内容
    attitude = db.Column(db.String(100))                # 情感分析：正向or负向

