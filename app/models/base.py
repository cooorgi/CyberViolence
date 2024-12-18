from app.extensions import db

class BaseModel(db.Model):
    __abstract__ = True  # 声明此类为抽象类，不会创建表

    id = db.Column(db.Integer, primary_key=True)        # ID
    nickname = db.Column(db.String(255))                # 用户名
    create_time = db.Column(db.String(255))             # 发布时间
    like_count = db.Column(db.Integer)                  # 点赞数/赞同数
    comment_count = db.Column(db.Integer)               # 评论数/二级评论数
    Year = db.Column(db.Integer)                        # 年
    Month = db.Column(db.Integer)                       # 月
    Day = db.Column(db.Integer)                         # 天
    TimePeriod = db.Column(db.String(255))              # 时间段



