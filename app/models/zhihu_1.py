from app.extensions import db



class zhihuContent():
    __tablename__ = 'washed_zhihu_content'              # 知乎帖子

    id = db.Column(db.String, primary_key=True)         # ID
    content_type = db.Column(db.String(255))            # 帖子类型
    content_text = db.Column(db.String(255))            # 帖子内容
    title = db.Column(db.String(255))                   # 帖子标题
    desc = db.Column(db.String(255))                    # 简介
    created_time = db.Column(db.String(255))            # 创建时间
    voteup_count = db.Column(db.String(255))            # 赞同数
    comment_count = db.Column(db.String(255))           # 评论数
    user_nickname = db.Column(db.String(255))           # 用户名
    Year = db.Column(db.Integer)                        # 年
    Month = db.Column(db.Integer)                       # 月
    Day = db.Column(db.Integer)                         # 日
    TimePeriod = db.Column(db.String(255))              # 时间段


class zhihuComment():
    __tablename__ = 'washed_zhihu_comment'              # 知乎帖子评论

    id = db.Column(db.String(255), primary_key=True)    # ID
    content = db.Column(db.String(255))                 # 评论内容
    publish_time = db.Column(db.String(255))            # 发布时间
    ip_location = db.Column(db.String(255))             # IP地址
    sub_comment_count = db.Column(db.String(255))       # 二级评论数
    like_count = db.Column(db.String(255))              # 赞同数
    dislike_count = db.Column(db.String(255))           # 反对数
    content_type = db.Column(db.String(255))            # 评论类型
    user_nickname = db.Column(db.String(255))           # 用户名
    Year = db.Column(db.Integer)                        # 年
    Month = db.Column(db.Integer)                       # 月
    Day = db.Column(db.Integer)                         # 日
    TimePeriod = db.Column(db.String(255))              # 时间段
    attitude = db.Column(db.String(100))                # 情感分析：正向or负向


