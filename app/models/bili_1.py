from app.extensions import db



class bilibiliVideo():
    __tablename__ = 'washed_bilibili_video'             # 清洗完的bilibili视频/帖子

    id = db.Column(db.String(255), primary_key=True)    # ID
    nickname = db.Column(db.String(255))                # 用户名
    title = db.Column(db.String(255))                   # 标题
    desc = db.Column(db.String(255))                    # 简介
    create_time = db.Column(db.TIMESTAMP)               # 发布时间
    liked_count = db.Column(db.String(255))             # 点赞数
    video_play_count = db.Column(db.String(255))        # 播放数
    video_danmaku = db.Column(db.String(255))           # 弹幕数
    video_comment = db.Column(db.String(255))           # 评论数
    Year = db.Column(db.Integer)                        # 年
    Month = db.Column(db.Integer)                       # 月
    Day = db.Column(db.Integer)                         # 天
    TimePeriod = db.Column(db.String(255))              # 时间段

class bilibiliVideoComment():
    __tablename__ = 'washed_bilibili_video_comment'     # 清洗完的bilibili视频/帖子评论

    id = db.Column(db.Integer, primary_key=True)        # ID
    nickname = db.Column(db.String(255))                # 用户名
    content = db.Column(db.String(255))                 # 评论内容
    create_time = db.Column(db.String(255))             # 发布时间
    sub_comment_count = db.Column(db.String(255))       # 二级评论数
    liked_count = db.Column(db.String(255))             # 点赞数
    Year = db.Column(db.Integer)                        # 年
    Month = db.Column(db.Integer)                       # 月
    Day = db.Column(db.Integer)                         # 日
    TimePeriod = db.Column(db.String(255))              # 时间段
    attitude = db.Column(db.String(100))                # 情感分析：正向or负向

