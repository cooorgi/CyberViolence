from decimal import Decimal

from flask import Blueprint, jsonify, render_template, make_response
from flask_cors import CORS
from sqlalchemy import func

from app import db
from app.models.zhihu import zhihuComment, zhihuContent

zhihu = Blueprint('zhihu', __name__)
CORS(zhihu)

@zhihu.route('/')
def index():
    return render_template('index.html')


@zhihu.route('/comment', methods=['GET'])
def commentCount():

    # 评论总数
    sum1 = db.session.query(func.sum(zhihuContent.comment_count)).scalar()
    sum2 = db.session.query(func.sum(zhihuComment.comment_count)).scalar()
    sum = sum1 + sum2

    data = {
        "count": sum,
    }
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@zhihu.route('/count', methods=['GET'])
def count():

    # 视频总数
    sum = db.session.query(func.count(zhihuContent.id)).scalar()
    data = {
        "count": sum,
    }
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@zhihu.route('/time', methods=['GET'])
def time():

    # 时间段
    a = db.session.query(func.count(zhihuContent.id)).filter(zhihuContent.TimePeriod == '凌晨').scalar()
    b = db.session.query(func.count(zhihuContent.id)).filter(zhihuContent.TimePeriod == '上午').scalar()
    c = db.session.query(func.count(zhihuContent.id)).filter(zhihuContent.TimePeriod == '下午').scalar()
    d = db.session.query(func.count(zhihuContent.id)).filter(zhihuContent.TimePeriod == '晚上').scalar()

    a += db.session.query(func.count(zhihuComment.id)).filter(zhihuComment.TimePeriod == '凌晨').scalar()
    b += db.session.query(func.count(zhihuComment.id)).filter(zhihuComment.TimePeriod == '上午').scalar()
    c += db.session.query(func.count(zhihuComment.id)).filter(zhihuComment.TimePeriod == '下午').scalar()
    d += db.session.query(func.count(zhihuComment.id)).filter(zhihuComment.TimePeriod == '晚上').scalar()

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

@zhihu.route("/heat", methods=['GET'])
def heat():

    # 查询热度前五的帖子
    results = db.session.query(
        zhihuContent.title,
        (2 * zhihuContent.like_count +
         3 * zhihuContent.comment_count
         ).label('heat')  # 计算热度
    ).order_by(func.coalesce((2 * zhihuContent.like_count +
                              3 * zhihuContent.comment_count
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


@zhihu.route("/heating", methods=['GET'])
def heating():

    # 每月热度总数

    # 计算视频每月的热度总数
    video_heat = db.session.query(
        zhihuContent.Year.label('year'),
        zhihuContent.Month.label('month'),
        func.sum(
            (2 * zhihuContent.like_count +
             3 * zhihuContent.comment_count)
        ).label('video_heat')
    ).group_by(
        zhihuContent.Year,
        zhihuContent.Month
    ).all()

    # 计算评论每月的热度总数
    comment_heat = db.session.query(
        zhihuComment.Year.label('year'),
        zhihuComment.Month.label('month'),
        func.sum(
            (1 * zhihuComment.like_count +
             1 * zhihuComment.dislike_count +
             1 * zhihuComment.comment_count)
        ).label('comment_heat')
    ).group_by(
        zhihuComment.Year,
        zhihuComment.Month
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


@zhihu.route("/mheating", methods=['GET'])
def heating_by_month():
    # 每月热度总数（只按月份，不考虑年份）

    # 计算视频每月的热度总数，按月份汇总
    video_heat = db.session.query(
        zhihuContent.Month.label('month'),
        func.sum(
            (2 * zhihuContent.like_count +
             3 * zhihuContent.comment_count)
        ).label('video_heat')
    ).group_by(
        zhihuContent.Month
    ).all()

    # 计算评论每月的热度总数，按月份汇总
    comment_heat = db.session.query(
        zhihuComment.Month.label('month'),
        func.sum(
            (1 * zhihuComment.like_count +
             1 * zhihuComment.dislike_count +
             1 * zhihuComment.comment_count)
        ).label('comment_heat')
    ).group_by(
        zhihuComment.Month
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


@zhihu.route("/total", methods=['GET'])
def total():

    # 情感统计
    a = db.session.query(func.count(zhihuComment.id)).filter(zhihuComment.attitude == "正向").scalar()
    b = db.session.query(func.count(zhihuComment.id)).filter(zhihuComment.attitude == "负向").scalar()
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

@zhihu.route("/positive", methods=['GET'])
def mypositive():
    # 统计每个月的正向情感评论数量
    positive_data = db.session.query(
        zhihuComment.Year.label('Year'),
        zhihuComment.Month.label('month'),
        func.count(zhihuComment.id).label('positive_count')
    ).filter(
        zhihuComment.attitude == "正向"
    ).group_by(
        zhihuComment.Year.label('Year'),
        zhihuComment.Month.label('month'),
    ).order_by(
        zhihuComment.Year.label('Year'),
        zhihuComment.Month.label('month'),
    ).all()

    # 查询每月的总评论数量
    total_data = db.session.query(
        zhihuComment.Year.label('Year'),
        zhihuComment.Month.label('month'),
        func.count(zhihuComment.id).label('total_count')
    ).group_by(
        zhihuComment.Year.label('Year'),
        zhihuComment.Month.label('month'),
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


@zhihu.route("/mpositive", methods=['GET'])
def mpositive():
    # 统计每个月的正向情感评论数量
    positive_data = db.session.query(
        zhihuComment.Month.label('month'),
        func.count(zhihuComment.id).label('positive_count')
    ).filter(
        zhihuComment.attitude == "正向"
    ).group_by(
        zhihuComment.Month.label('month'),
    ).order_by(
        zhihuComment.Month.label('month'),
    ).all()

    # 查询每月的总评论数量
    total_data = db.session.query(
        zhihuComment.Month.label('month'),
        func.count(zhihuComment.id).label('total_count')
    ).group_by(
        zhihuComment.Month.label('month'),
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


@zhihu.route("/ip", methods=['GET'])
def ip():
    # 统计帖子热度，按 ip_location 分组
    ip_heat = db.session.query(
        zhihuContent.ip_location.label('ip_location'),
        func.sum(
            2 * zhihuContent.like_count +
            3 * zhihuContent.comment_count
        ).label('video_heat')
    ).group_by(zhihuContent.ip_location).all()

    # 统计评论热度，按 ip_location 分组
    comment_heat_by_ip_location = db.session.query(
        zhihuComment.ip_location.label('ip_location'),
        func.sum(
            1 * zhihuComment.like_count +
            1 * zhihuComment.dislike_count +
            1 * zhihuComment.comment_count
        ).label('comment_heat')
    ).group_by(zhihuComment.ip_location).all()

    # 合并数据
    heat_by_ip_location = {}
    for ip_location, heat in ip_heat:
        if ip_location not in heat_by_ip_location:
            heat_by_ip_location[ip_location] = {"video_heat": 0, "comment_heat": 0}
        heat_by_ip_location[ip_location]["video_heat"] = float(heat)

    for ip_location, heat in comment_heat_by_ip_location:
        if ip_location not in heat_by_ip_location:
            heat_by_ip_location[ip_location] = {"video_heat": 0, "comment_heat": 0}
        heat_by_ip_location[ip_location]["comment_heat"] = float(heat)

    # 构造响应数据
    data = []
    for ip_location, heat in heat_by_ip_location.items():
        total_heat = heat["video_heat"] + heat["comment_heat"]
        data.append({
            "region_name": ip_location,
            "heat_value": total_heat
        })

    # 排序：按总热度降序
    data.sort(key=lambda x: x["heat_value"], reverse=True)

    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response
