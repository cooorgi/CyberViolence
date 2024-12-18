from decimal import Decimal

from flask import Blueprint, render_template, make_response, jsonify
from flask_cors import CORS
from sqlalchemy import func, extract
from app.extensions import db
from app.models import bilibiliVideo, bilibiliVideoComment

bili = Blueprint('bilibili', __name__)
CORS(bili)

@bili.route('/')
def index():
    return render_template('index.html')


@bili.route('/comment', methods=['GET'])
def commentCount():

    # 评论总数
    sum1 = db.session.query(func.sum(bilibiliVideo.comment_count)).scalar()
    sum2 = db.session.query(func.sum(bilibiliVideoComment.comment_count)).scalar()
    sum = sum1 + sum2

    data = {
        "count": sum,
    }
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@bili.route('/count', methods=['GET'])
def count():

    # 视频总数
    sum = db.session.query(func.count(bilibiliVideo.id)).scalar()
    data = {
        "count": sum,
    }
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@bili.route('/time', methods=['GET'])
def time():

    # 时间段
    a = db.session.query(func.count(bilibiliVideo.id)).filter(bilibiliVideo.TimePeriod == '凌晨').scalar()
    b = db.session.query(func.count(bilibiliVideo.id)).filter(bilibiliVideo.TimePeriod == '上午').scalar()
    c = db.session.query(func.count(bilibiliVideo.id)).filter(bilibiliVideo.TimePeriod == '下午').scalar()
    d = db.session.query(func.count(bilibiliVideo.id)).filter(bilibiliVideo.TimePeriod == '晚上').scalar()

    a += db.session.query(func.count(bilibiliVideoComment.id)).filter(bilibiliVideoComment.TimePeriod == '凌晨').scalar()
    b += db.session.query(func.count(bilibiliVideoComment.id)).filter(bilibiliVideoComment.TimePeriod == '上午').scalar()
    c += db.session.query(func.count(bilibiliVideoComment.id)).filter(bilibiliVideoComment.TimePeriod == '下午').scalar()
    d += db.session.query(func.count(bilibiliVideoComment.id)).filter(bilibiliVideoComment.TimePeriod == '晚上').scalar()

    data = [
        {
            "time_period": "凌晨",
            "value": a,
        },
        {
            "time_period": "上午",
            "value": b,
        },
        {
            "time_period": "下午",
            "value": c,
        },
        {
            "time_period": "晚上",
            "value": d,
        },
    ]
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@bili.route("/heat", methods=['GET'])
def heat():

    # 查询热度前五的帖子
    results = db.session.query(
        bilibiliVideo.title,
        (1 * bilibiliVideo.like_count +
         1.5 * bilibiliVideo.video_play_count +
         2 * bilibiliVideo.video_danmaku +
         2 * bilibiliVideo.comment_count
         ).label('heat')  # 计算热度
    ).order_by(func.coalesce((1 * bilibiliVideo.like_count +
                              1.5 * bilibiliVideo.video_play_count +
                              2 * bilibiliVideo.video_danmaku +
                              2 * bilibiliVideo.comment_count
                              ), 0).desc()).limit(5).all()

    top_posts = [
        {
            "content": result.title,
            "heat": result.heat
        }
        for result in results
    ]

    response = make_response(jsonify(top_posts), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@bili.route("/heating", methods=['GET'])
def heating():

    # 每月热度总数

    # 计算视频每月的热度总数
    video_heat = db.session.query(
        bilibiliVideo.Year.label('year'),
        bilibiliVideo.Month.label('month'),
        func.sum(
            (1 * bilibiliVideo.like_count +
             1.5 * bilibiliVideo.video_play_count +
             2 * bilibiliVideo.video_danmaku +
             2 * bilibiliVideo.comment_count)
        ).label('video_heat')
    ).group_by(
        bilibiliVideo.Year,
        bilibiliVideo.Month
    ).all()

    # 计算评论每月的热度总数
    comment_heat = db.session.query(
        bilibiliVideoComment.Year.label('year'),
        bilibiliVideoComment.Month.label('month'),
        func.sum(
            (1 * bilibiliVideoComment.like_count +
             2 * bilibiliVideoComment.comment_count)
        ).label('comment_heat')
    ).group_by(
        bilibiliVideoComment.Year,
        bilibiliVideoComment.Month
    ).all()

    # 合并视频和评论的热度数据
    combined_heat = {}
    for year, month, heat in video_heat:
        if (year, month) not in combined_heat:
            combined_heat[(year, month)] = {'video_heat': Decimal(0), 'comment_heat': Decimal(0)}
        combined_heat[(year, month)]['video_heat'] = Decimal(heat)

    for year, month, heat in comment_heat:
        if (year, month) not in combined_heat:
            combined_heat[(year, month)] = {'video_heat': Decimal(0), 'comment_heat': Decimal(0)}
        combined_heat[(year, month)]['comment_heat'] = Decimal(heat)

    # 计算每个月的总热度
    monthly_heat = []
    for (year, month), heat_data in combined_heat.items():
        total_heat = heat_data['video_heat'] + heat_data['comment_heat']
        monthly_heat.append({
            'year': year,
            'month': month,
            'total_heat': total_heat
        })

    monthly_heat.sort(key=lambda x: (x["year"], x["month"]))

    response = make_response(jsonify(monthly_heat), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@bili.route("/mheating", methods=['GET'])
def heating_by_month():
    # 每月热度总数（只按月份，不考虑年份）

    # 计算视频每月的热度总数，按月份汇总
    video_heat = db.session.query(
        bilibiliVideo.Month.label('month'),
        func.sum(
            (1 * bilibiliVideo.like_count +
             1.5 * bilibiliVideo.video_play_count +
             2 * bilibiliVideo.video_danmaku +
             2 * bilibiliVideo.comment_count)
        ).label('video_heat')
    ).group_by(
        bilibiliVideo.Month
    ).all()

    # 计算评论每月的热度总数，按月份汇总
    comment_heat = db.session.query(
        bilibiliVideoComment.Month.label('month'),
        func.sum(
            (1 * bilibiliVideoComment.like_count +
             2 * bilibiliVideoComment.comment_count)
        ).label('comment_heat')
    ).group_by(
        bilibiliVideoComment.Month
    ).all()

    # 合并视频和评论的热度数据
    combined_heat = {}
    for month, heat in video_heat:
        if month not in combined_heat:
            combined_heat[month] = {'video_heat': Decimal(0), 'comment_heat': Decimal(0)}
        combined_heat[month]['video_heat'] = Decimal(heat)

    for month, heat in comment_heat:
        if month not in combined_heat:
            combined_heat[month] = {'video_heat': Decimal(0), 'comment_heat': Decimal(0)}
        combined_heat[month]['comment_heat'] = Decimal(heat)

    # 计算每个月的总热度
    monthly_heat = []
    for month, heat_data in combined_heat.items():
        total_heat = heat_data['video_heat'] + heat_data['comment_heat']
        monthly_heat.append({
            'month': month,
            'total_heat': total_heat
        })

    monthly_heat.sort(key=lambda x: (x["month"]))
    response = make_response(jsonify(monthly_heat), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@bili.route("/total", methods=['GET'])
def total():

    # 情感统计
    a = db.session.query(func.count(bilibiliVideoComment.id)).filter(bilibiliVideoComment.attitude == "正向").scalar()
    b = db.session.query(func.count(bilibiliVideoComment.id)).filter(bilibiliVideoComment.attitude == "负向").scalar()
    data = {
        "series": [
            {
                "value": a,
                "name": "正向"
            },
            {
                "value": b,
                "name": "负向"
            },
        ]
    }
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@bili.route("/positive", methods=['GET'])
def mypositive():
    # 统计每个月的正向情感评论数量
    positive_data = db.session.query(
        bilibiliVideoComment.Year.label('Year'),
        bilibiliVideoComment.Month.label('month'),
        func.count(bilibiliVideoComment.id).label('positive_count')
    ).filter(
        bilibiliVideoComment.attitude == "正向"
    ).group_by(
        bilibiliVideoComment.Year.label('Year'),
        bilibiliVideoComment.Month.label('month'),
    ).order_by(
        bilibiliVideoComment.Year.label('Year'),
        bilibiliVideoComment.Month.label('month'),
    ).all()

    # 查询每月的总评论数量
    total_data = db.session.query(
        bilibiliVideoComment.Year.label('Year'),
        bilibiliVideoComment.Month.label('month'),
        func.count(bilibiliVideoComment.id).label('total_count')
    ).group_by(
        bilibiliVideoComment.Year.label('Year'),
        bilibiliVideoComment.Month.label('month'),
    ).all()

    # 整合正向评论和总评论数据
    monthly_stats = {}
    for year, month, count in total_data:
        monthly_stats[(year, month)] = {"total_count": int(count), "positive_count": 0}

    for year, month, count in positive_data:
        if (year, month) in monthly_stats:
            monthly_stats[(year, month)]["positive_count"] = int(count)
        else:
            monthly_stats[(year, month)] = {"total_count": 0, "positive_count": int(count)}

    # 格式化输出
    data = []
    for (year, month), counts in monthly_stats.items():
        data.append({
            "year": year,
            "month": month,
            "positive": counts["positive_count"],
            "total": counts["total_count"]
        })

    data.sort(key=lambda x: (x["year"], x["month"]))

    # 生成响应
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@bili.route("/mpositive", methods=['GET'])
def mpositive():
    # 统计每个月的正向情感评论数量
    positive_data = db.session.query(
        bilibiliVideoComment.Month.label('month'),
        func.count(bilibiliVideoComment.id).label('positive_count')
    ).filter(
        bilibiliVideoComment.attitude == "正向"
    ).group_by(
        bilibiliVideoComment.Month.label('month'),
    ).order_by(
        bilibiliVideoComment.Month.label('month'),
    ).all()

    # 查询每月的总评论数量
    total_data = db.session.query(
        bilibiliVideoComment.Month.label('month'),
        func.count(bilibiliVideoComment.id).label('total_count')
    ).group_by(
        bilibiliVideoComment.Month.label('month'),
    ).all()

    # 整合正向评论和总评论数据
    monthly_stats = {}
    for month, count in total_data:
        monthly_stats[month] = {"total_count": int(count), "positive_count": 0}

    for month, count in positive_data:
        if month in monthly_stats:
            monthly_stats[month]["positive_count"] = int(count)
        else:
            monthly_stats[month] = {"total_count": 0, "positive_count": int(count)}

    # 格式化输出
    data = []
    for month, counts in monthly_stats.items():
        data.append({
            "month": month,
            "positive": counts["positive_count"],
            "total": counts["total_count"],
        })

    data.sort(key=lambda x: (x["month"]))

    # 生成响应
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response


