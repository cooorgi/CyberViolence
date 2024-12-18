from app.extensions import db



class xhsNoteComment():
    __tablename__ = 'washed_xhs_note_comment'       # 小红书帖子评论

    id = db.Column(db.Integer, primary_key=True)    # ID
    nickname = db.Column(db.String(255))            # 用户名
    ip_location =db.Column(db.String(255))          # IP地址
    create_time = db.Column(db.String(255))         # 发布时间
    content = db.Column(db.String(255))             # 评论内容
    sub_comment_count = db.Column(db.String(255))   # 二级评论数
    like_count = db.Column(db.String(255))          # 点赞数
    Year = db.Column(db.Integer)                    # 年
    Month = db.Column(db.Integer)                   # 月
    Day = db.Column(db.Integer)                     # 天
    TimePeriod = db.Column(db.String(255))          # 时间段
    attitude = db.Column(db.String(100))            # 情感分析：正向or负向

class xhsNote():
    __tablename__ = 'washed_xhs_note'               # 小红书帖子

    id = db.Column(db.Integer, primary_key=True)    # ID
    nickname = db.Column(db.String(255))            # 用户名
    ip_location = db.Column(db.String(255))         # IP地址
    type = db.Column(db.String(255))                # 帖子类型
    title = db.Column(db.String(255))               # 标题
    desc = db.Column(db.String(255))                # 简介
    time = db.Column(db.String(255))                # 发布时间
    liked_count = db.Column(db.Integer)             # 点赞数
    collected_count = db.Column(db.Integer)         # 收藏数
    comment_count = db.Column(db.Integer)           # 评论数
    share_count = db.Column(db.Integer)             # 分享数
    tag_list = db.Column(db.String(255))            # 分类标签
    year = db.Column(db.Integer)                    # 年
    month = db.Column(db.Integer)                   # 月
    day = db.Column(db.Integer)                     # 日
    time_period = db.Column(db.String(255))         # 时间段
    platform = db.Column(db.String(255))            # 来源

