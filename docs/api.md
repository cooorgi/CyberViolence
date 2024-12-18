### 所需的东西2.0

全部的接口及相关都在index.js中

###### 这是热度计算公式，难搞就变成数量

```c++
//小红书
1.note(贴子)
根据liked_count，collected_count，comment_count计算
    以heat=1*liked_count+2*collected_count+2*comment_count+2*shared_count为数据基底
2.comment(评论)
据sub_comment_count，like_count来计算
    以heat=1+like_count+1.5*sub_comment_count为数据基底

//知乎
1.content(帖子/内容)
根据voteup_count,comment_count来计算
    以heat=2*voteup_count+3*comment_count为数据基底
2.comment
根据sub_comment_count,like_count,dislike_count来计算
    以heat=like_count+dislike_count+sub_comment_count为数据基底
//Bilibili
1.Video(视频)
根据liked_count,video_play_count,video_danmaku,video_comment来计算
    以heat=1*like_count+1.5*video_play_count+2*video_danmaku+2*video_comment为数据基底
2.comment
据sub_comment_count，like_count来计算
    以heat=1*like_count+1.5*sub_comment_count为数据基底
```



##### 1.各个平台的视频||帖子数量

```json
json格式如下
{ "count": 12345 }

B站：785
小红书：448
知乎：420
total：1653
```

##### 2.各个平台的评论数**应为评论数+视频下评论数

```json
json格式如下
{ "count": 12345 }
B站：137646+1245831
小红：1886+53578
知乎：2119+28567
total：1469627
```

##### 3.各个平台的热度的排名前五？

```json
json格式如下
[
	{ "name": "话题1", "value": 100 },
	{ "name": "话题2", "value": 200 },
	...
]
    
```

B站

```
29229955	被“实锤”家暴、视频造假将近一年，我是怎么回应的？
11511422	【罗翔】聊聊网络喷子与键盘侠
13519396.5	还原一下著名的《潘博文事件》
11395927	触目惊心！缅北诈骗集团内部视频流出。。。
10316862.5	究竟网络暴力带来了什么？
```

小红书

```
1058788	网络暴力我们该如何自救，希望你们永远遇不到#酸菜日记[话题]#??#真实事件改编[话题]#??#情感共鸣[话题]#
72373.5	帮主播怼赢键盘侠
53100.5	发疯后续·妈妈视奸，被“网络暴力”气哭了
27500	最近我注意到了这类网络现象，所以画了下来。 遇到网暴，有些人可能会和漫画中的人一样，成为那个自己不喜欢的人，也有的人可能会因此消失不见，还有的人仍然在坚持自己的梦想。 我想告诉那些喜欢画画的朋友们，遇到网络上恶意的攻击和言论，应该继续努力去做你该做的事情。 #网络暴力[话题]# #漫画[话题]# #绘画[话题]#
23684	如果你被网暴了，请你这样做??
```

知乎

```
22015	成都大学党委书记毛洪涛遗体已被找到，案件还有哪些值得关注的信息？
21201	你见过的男生，可以有多坏？
19044.5	14岁少女被键盘侠逼死，父亲邀请凶手参加葬礼：网络暴力有多可怕？（知乎1.4万高赞）
12664	如何评价中国政法大学罗翔教授？
12562	对蔡徐坤的黑是否过度已构成网络暴力？
```



##### 4.热度变化--每个月的热度

```json
{
	"xAxis": ["1月", "2月", "3月", ...],
	"values": [24, 40, 101, ...]//热度
 }

```

B站

```
15459201.5+330271	=15789472.5
11909823+730997.5	=12640820.5
16173754+704913		=16878667
12091610.5+795808	=12887418.5
11843453+390944		=12234397
8978444+506178.5	=9484622.5
19913990+573488		=20487478
23991928+984503		=24976431
9677722.5+470330	=10148052.5
18133815+392047		=18525862
26289510+396451		=26685961
11760400+293961.5	=12054361.5
```

小红书

```
2009.5+72		=2081.5
17954+421.5		=18375.5
39515+52.5		=39567.5
30204.5+184.5	=30389
36526+3231		=39757
71133+505.5		=71638.5
23713.5+314		=24027.5
103700+996		=104696
1093205+803.5	=1094008.5
65867+2067		=67934
136683+1078		=137761
76201.5+73		=76274.5
```

知乎

```
61187+10865.5	=72052.5
12530+16795		=29325
11159+2400		=13559
35241+3057.5	=38298.5
13239+7134		=20373
10243.5+1150.5	=11394
21193+2718.5	=23911.5
17178.5+2595	=19773.5
1493.5+361		=1854.5
60007.5+2626.5	=62634
15236+1714.5	=16950.5
41518.5+2701.5	=44220
```



##### 5.情感类数量（total）

```json
{
	"series": [
		{ "value": 30, "name": "正面" },
		{ "value": 50, "name": "负面" },
		{ "value": 20, "name": "else" }
	]
}
```

B站 正--负

```
36008
101638
```

小红书 正--负

```
358
1528
```

知乎 正--负

```
487
1632
```

合计 正--负

```
36853
104798
```



##### 6.情感类数量（月&平台）

```json
{
	"monthly": [
		{ "month": 1, "positive": 30, "total": 100 },
		{ "month": 1, "positive": 40, "total": 120 },
		...
	]
}
```

B站

```
1814/6750	=0.2687407407
2006/8477	=0.2366403209
2747/12173	=0.2256633533
3941/14559	=0.2706916684
2539/9194	=0.2761583642
2879/13329	=0.2159951984
3983/13890	=0.2867530598
6155/23265	=0.2645604986
2942/10528	=0.2794452888
2533/8782	=0.2884308813
2911/10615	=0.2742345737
1558/6084	=0.2560815253
```

小红书

```
2/15		=0.1333333333
21/183		=0.1147540984
8/36		=0.2222222222
12/78		=0.1538461538
61/312		=0.1955128205
20/153		=0.1307189542
9/62		=0.1451612903
61/258		=0.2364341085
45/175		=0.2571428571
58/291		=0.1993127148
56/304		=0.1842105263
5/19		=0.2631578947
```

知乎

```
53/270	=0.1962962963
45/221	=0.2036199095
39/138	=0.2826086957
35/174	=0.2011494253
63/271	=0.2324723247
35/188	=0.1861702128
27/122	=0.2213114754
49/236	=0.2076271186
15/86	=0.1744186047
44/126	=0.3492063492
50/190	=0.2631578947
32/97	=0.2631578947
```



##### 7.时间段统计（total）

```json
{
    { "time_period": "早上", "value": 10 },
    { "time_period": "下午", "value": 20 },
    { "time_period": "晚上", "value": 15 },
    { "time_period": "凌晨", "value": 5 }
}
```

B站 凌晨-早上-下午-晚上

```
18515
27960
42889
48282
```

小红书 凌晨-早上-下午-晚上

```
294
413
582
597
```

知乎 凌晨-早上-下午-晚上

```
274
541
679
625
```

合计 凌晨-早上-下午-晚上

```
19083
28914
44150
49504
```

##### 8.ip的热度

```json
//json的格式，改参数名字无所谓 
[
    { "region_name": "北京", "heat_value": 1000 },
    { "region_name": "上海", "heat_value": 800 },
    { "region_name": "广东", "heat_value": 1200 }
]
 
```

云》粤》豫》川》京



## 接口

| 接口                | 备注                                                 |
| ------------------- | ---------------------------------------------------- |
| /bilibili/comment   | 评论总数                                             |
| /bilibili/count     | 视频总数                                             |
| /bilibili/time      | 时间段                                               |
| /bilibili/heat      | 查询热度前五的帖子                                   |
| /bilibili/heating   | 每月热度总数                                         |
| /bilibili/mheating  | 每月热度总数（只按月份，不考虑年份）                 |
| /bilibili/total     | 情感统计                                             |
| /bilibili/positive  | 统计每个月的正向情感评论数量                         |
| /bilibili/mpositive | 统计每个月的正向情感评论数量（只按月份，不考虑年份） |
| /xhs/ip             |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |
|                     |                                                      |

### 返回值示例

### /bilibili/comment

```
{
    "count": "1459162"
}
```

### /bilibili/count

```
{
    "count": 785
}
```

### /bilibili/time

```
[
{
"time_period": "凌晨",
"value": 16965
},
{
"time_period": "上午",
"value": 25211
},
{
"time_period": "下午",
"value": 39243
},
{
"time_period": "晚上",
"value": 44512
}
]
```

### /bilibili/heat

```
[
{
"content": "被“实锤”家暴、视频造假将近一年，我是怎么回应的？",
"heat": 41227406
},
{
"content": "【罗翔】聊聊网络喷子与键盘侠",
"heat": 22274991
},
{
"content": "还原一下著名的《潘博文事件》",
"heat": 19849808.5
},
{
"content": "触目惊心！缅北诈骗集团内部视频流出。。。",
"heat": 16472705
},
{
"content": "究竟网络暴力带来了什么？",
"heat": 14332962.5
}
]
```

### /bilibili/heating

```
[
{
"month": 8,
"total_heat": "606929",
"year": 2015
},
{
"month": 9,
"total_heat": "45951.5",
"year": 2015
},
{
"month": 10,
"total_heat": "7",
"year": 2015
},
{
"month": 12,
"total_heat": "0",
"year": 2015
},
{
"month": 1,
"total_heat": "55",
"year": 2016
},
{
"month": 3,
"total_heat": "5",
"year": 2016
},
{
"month": 4,
"total_heat": "1",
"year": 2016
},
{
"month": 5,
"total_heat": "25",
"year": 2016
},
{
"month": 6,
"total_heat": "4",
"year": 2016
},
{
"month": 7,
"total_heat": "34",
"year": 2016
},
{
"month": 8,
"total_heat": "78075.5",
"year": 2016
},
{
"month": 9,
"total_heat": "13",
"year": 2016
},
{
"month": 10,
"total_heat": "4921162",
"year": 2016
},
{
"month": 11,
"total_heat": "491",
"year": 2016
},
{
"month": 12,
"total_heat": "294",
"year": 2016
},
{
"month": 1,
"total_heat": "1404",
"year": 2017
},
{
"month": 2,
"total_heat": "408",
"year": 2017
},
{
"month": 3,
"total_heat": "144247",
"year": 2017
},
{
"month": 4,
"total_heat": "44058",
"year": 2017
},
{
"month": 5,
"total_heat": "249",
"year": 2017
},
{
"month": 6,
"total_heat": "24872.5",
"year": 2017
},
{
"month": 7,
"total_heat": "793392.5",
"year": 2017
},
{
"month": 8,
"total_heat": "689665",
"year": 2017
},
{
"month": 9,
"total_heat": "1871",
"year": 2017
},
{
"month": 10,
"total_heat": "138548",
"year": 2017
},
{
"month": 11,
"total_heat": "1177",
"year": 2017
},
{
"month": 12,
"total_heat": "623095",
"year": 2017
},
{
"month": 1,
"total_heat": "459",
"year": 2018
},
{
"month": 2,
"total_heat": "623",
"year": 2018
},
{
"month": 3,
"total_heat": "1965",
"year": 2018
},
{
"month": 4,
"total_heat": "54974.5",
"year": 2018
},
{
"month": 5,
"total_heat": "242819.5",
"year": 2018
},
{
"month": 6,
"total_heat": "879227.5",
"year": 2018
},
{
"month": 7,
"total_heat": "33519",
"year": 2018
},
{
"month": 8,
"total_heat": "887",
"year": 2018
},
{
"month": 9,
"total_heat": "42929",
"year": 2018
},
{
"month": 10,
"total_heat": "2073",
"year": 2018
},
{
"month": 11,
"total_heat": "785",
"year": 2018
},
{
"month": 12,
"total_heat": "129875.5",
"year": 2018
},
{
"month": 1,
"total_heat": "1003118",
"year": 2019
},
{
"month": 2,
"total_heat": "32244.5",
"year": 2019
},
{
"month": 3,
"total_heat": "150783.5",
"year": 2019
},
{
"month": 4,
"total_heat": "1320189",
"year": 2019
},
{
"month": 5,
"total_heat": "865501.5",
"year": 2019
},
{
"month": 6,
"total_heat": "5789657.5",
"year": 2019
},
{
"month": 7,
"total_heat": "10887156",
"year": 2019
},
{
"month": 8,
"total_heat": "6119786",
"year": 2019
},
{
"month": 9,
"total_heat": "10073.5",
"year": 2019
},
{
"month": 10,
"total_heat": "3953099",
"year": 2019
},
{
"month": 11,
"total_heat": "9688031",
"year": 2019
},
{
"month": 12,
"total_heat": "4722943.5",
"year": 2019
},
{
"month": 1,
"total_heat": "150183",
"year": 2020
},
{
"month": 2,
"total_heat": "7491100.5",
"year": 2020
},
{
"month": 3,
"total_heat": "5312511",
"year": 2020
},
{
"month": 4,
"total_heat": "23929096",
"year": 2020
},
{
"month": 5,
"total_heat": "11282787",
"year": 2020
},
{
"month": 6,
"total_heat": "110049.5",
"year": 2020
},
{
"month": 7,
"total_heat": "2568524.5",
"year": 2020
},
{
"month": 8,
"total_heat": "4576617",
"year": 2020
},
{
"month": 9,
"total_heat": "3746498.5",
"year": 2020
},
{
"month": 10,
"total_heat": "440732.5",
"year": 2020
},
{
"month": 11,
"total_heat": "45665.5",
"year": 2020
},
{
"month": 12,
"total_heat": "16841101.5",
"year": 2020
},
{
"month": 1,
"total_heat": "1758162.5",
"year": 2021
},
{
"month": 2,
"total_heat": "1127",
"year": 2021
},
{
"month": 3,
"total_heat": "8303160",
"year": 2021
},
{
"month": 4,
"total_heat": "2667117.5",
"year": 2021
},
{
"month": 5,
"total_heat": "8498043.5",
"year": 2021
},
{
"month": 6,
"total_heat": "151118.5",
"year": 2021
},
{
"month": 7,
"total_heat": "2491721",
"year": 2021
},
{
"month": 8,
"total_heat": "44889441",
"year": 2021
},
{
"month": 9,
"total_heat": "5594213",
"year": 2021
},
{
"month": 10,
"total_heat": "1766490.5",
"year": 2021
},
{
"month": 11,
"total_heat": "2764571",
"year": 2021
},
{
"month": 12,
"total_heat": "1742806",
"year": 2021
},
{
"month": 1,
"total_heat": "4745248.5",
"year": 2022
},
{
"month": 2,
"total_heat": "85969.5",
"year": 2022
},
{
"month": 3,
"total_heat": "1874879",
"year": 2022
},
{
"month": 4,
"total_heat": "6246867",
"year": 2022
},
{
"month": 5,
"total_heat": "41430.5",
"year": 2022
},
{
"month": 6,
"total_heat": "3008754.5",
"year": 2022
},
{
"month": 7,
"total_heat": "20068890.5",
"year": 2022
},
{
"month": 8,
"total_heat": "8786377",
"year": 2022
},
{
"month": 9,
"total_heat": "19934780.5",
"year": 2022
},
{
"month": 10,
"total_heat": "5577465",
"year": 2022
},
{
"month": 11,
"total_heat": "7212619",
"year": 2022
},
{
"month": 12,
"total_heat": "3665760.5",
"year": 2022
},
{
"month": 1,
"total_heat": "8770430",
"year": 2023
},
{
"month": 2,
"total_heat": "15570269",
"year": 2023
},
{
"month": 3,
"total_heat": "16309143.5",
"year": 2023
},
{
"month": 4,
"total_heat": "20706184",
"year": 2023
},
{
"month": 5,
"total_heat": "4000705",
"year": 2023
},
{
"month": 6,
"total_heat": "6727846",
"year": 2023
},
{
"month": 7,
"total_heat": "11630767",
"year": 2023
},
{
"month": 8,
"total_heat": "28221418",
"year": 2023
},
{
"month": 9,
"total_heat": "16049347.5",
"year": 2023
},
{
"month": 10,
"total_heat": "1880411.5",
"year": 2023
},
{
"month": 11,
"total_heat": "5641724.5",
"year": 2023
},
{
"month": 12,
"total_heat": "2940327.5",
"year": 2023
},
{
"month": 1,
"total_heat": "5766253.5",
"year": 2024
},
{
"month": 2,
"total_heat": "1852469.5",
"year": 2024
},
{
"month": 3,
"total_heat": "3133322.5",
"year": 2024
},
{
"month": 4,
"total_heat": "4772540",
"year": 2024
},
{
"month": 5,
"total_heat": "17929897.5",
"year": 2024
},
{
"month": 6,
"total_heat": "9614700",
"year": 2024
},
{
"month": 7,
"total_heat": "14862976",
"year": 2024
},
{
"month": 8,
"total_heat": "14204134.5",
"year": 2024
},
{
"month": 9,
"total_heat": "2847421",
"year": 2024
},
{
"month": 10,
"total_heat": "16048767.5",
"year": 2024
},
{
"month": 11,
"total_heat": "23241352.5",
"year": 2024
}
]
```

### /bilibili/mheating

```
[
{
"month": 1,
"total_heat": "22195313.5"
},
{
"month": 2,
"total_heat": "25034211"
},
{
"month": 3,
"total_heat": "35230016.5"
},
{
"month": 4,
"total_heat": "59741027"
},
{
"month": 5,
"total_heat": "42861458.5"
},
{
"month": 6,
"total_heat": "26306230"
},
{
"month": 7,
"total_heat": "63336980.5"
},
{
"month": 8,
"total_heat": "108173330"
},
{
"month": 9,
"total_heat": "48273098.5"
},
{
"month": 10,
"total_heat": "34728756"
},
{
"month": 11,
"total_heat": "48596416.5"
},
{
"month": 12,
"total_heat": "30666203.5"
}
]
```

### /bilibili/total

```
{
"series": [
{
"name": "正向",
"value": 32795
},
{
"name": "负向",
"value": 92351
}
]
}
```

### /bilibili/positive

```
[
{
"month": 8,
"positive": 76,
"total": 204,
"year": 2015
},
{
"month": 9,
"positive": 5,
"total": 14,
"year": 2015
},
{
"month": 10,
"positive": 3,
"total": 4,
"year": 2015
},
{
"month": 12,
"positive": 0,
"total": 1,
"year": 2015
},
{
"month": 1,
"positive": 2,
"total": 5,
"year": 2016
},
{
"month": 3,
"positive": 1,
"total": 1,
"year": 2016
},
{
"month": 4,
"positive": 3,
"total": 3,
"year": 2016
},
{
"month": 5,
"positive": 2,
"total": 2,
"year": 2016
},
{
"month": 6,
"positive": 0,
"total": 3,
"year": 2016
},
{
"month": 7,
"positive": 2,
"total": 2,
"year": 2016
},
{
"month": 8,
"positive": 4,
"total": 7,
"year": 2016
},
{
"month": 9,
"positive": 1,
"total": 3,
"year": 2016
},
{
"month": 10,
"positive": 470,
"total": 983,
"year": 2016
},
{
"month": 11,
"positive": 22,
"total": 52,
"year": 2016
},
{
"month": 12,
"positive": 19,
"total": 34,
"year": 2016
},
{
"month": 1,
"positive": 13,
"total": 30,
"year": 2017
},
{
"month": 2,
"positive": 8,
"total": 15,
"year": 2017
},
{
"month": 3,
"positive": 2,
"total": 9,
"year": 2017
},
{
"month": 4,
"positive": 5,
"total": 11,
"year": 2017
},
{
"month": 5,
"positive": 7,
"total": 20,
"year": 2017
},
{
"month": 6,
"positive": 6,
"total": 14,
"year": 2017
},
{
"month": 7,
"positive": 178,
"total": 519,
"year": 2017
},
{
"month": 8,
"positive": 210,
"total": 1085,
"year": 2017
},
{
"month": 9,
"positive": 30,
"total": 138,
"year": 2017
},
{
"month": 10,
"positive": 27,
"total": 92,
"year": 2017
},
{
"month": 11,
"positive": 18,
"total": 83,
"year": 2017
},
{
"month": 12,
"positive": 137,
"total": 691,
"year": 2017
},
{
"month": 1,
"positive": 22,
"total": 48,
"year": 2018
},
{
"month": 2,
"positive": 11,
"total": 37,
"year": 2018
},
{
"month": 3,
"positive": 7,
"total": 30,
"year": 2018
},
{
"month": 4,
"positive": 10,
"total": 46,
"year": 2018
},
{
"month": 5,
"positive": 12,
"total": 40,
"year": 2018
},
{
"month": 6,
"positive": 24,
"total": 86,
"year": 2018
},
{
"month": 7,
"positive": 14,
"total": 46,
"year": 2018
},
{
"month": 8,
"positive": 17,
"total": 64,
"year": 2018
},
{
"month": 9,
"positive": 6,
"total": 36,
"year": 2018
},
{
"month": 10,
"positive": 20,
"total": 85,
"year": 2018
},
{
"month": 11,
"positive": 11,
"total": 52,
"year": 2018
},
{
"month": 12,
"positive": 9,
"total": 40,
"year": 2018
},
{
"month": 1,
"positive": 181,
"total": 404,
"year": 2019
},
{
"month": 2,
"positive": 22,
"total": 105,
"year": 2019
},
{
"month": 3,
"positive": 11,
"total": 51,
"year": 2019
},
{
"month": 4,
"positive": 61,
"total": 216,
"year": 2019
},
{
"month": 5,
"positive": 11,
"total": 75,
"year": 2019
},
{
"month": 6,
"positive": 252,
"total": 953,
"year": 2019
},
{
"month": 7,
"positive": 155,
"total": 962,
"year": 2019
},
{
"month": 8,
"positive": 185,
"total": 736,
"year": 2019
},
{
"month": 9,
"positive": 55,
"total": 213,
"year": 2019
},
{
"month": 10,
"positive": 42,
"total": 143,
"year": 2019
},
{
"month": 11,
"positive": 389,
"total": 1687,
"year": 2019
},
{
"month": 12,
"positive": 191,
"total": 590,
"year": 2019
},
{
"month": 1,
"positive": 95,
"total": 286,
"year": 2020
},
{
"month": 2,
"positive": 355,
"total": 948,
"year": 2020
},
{
"month": 3,
"positive": 538,
"total": 3214,
"year": 2020
},
{
"month": 4,
"positive": 1680,
"total": 5819,
"year": 2020
},
{
"month": 5,
"positive": 982,
"total": 2751,
"year": 2020
},
{
"month": 6,
"positive": 162,
"total": 687,
"year": 2020
},
{
"month": 7,
"positive": 509,
"total": 1875,
"year": 2020
},
{
"month": 8,
"positive": 526,
"total": 1944,
"year": 2020
},
{
"month": 9,
"positive": 281,
"total": 1454,
"year": 2020
},
{
"month": 10,
"positive": 383,
"total": 1637,
"year": 2020
},
{
"month": 11,
"positive": 46,
"total": 131,
"year": 2020
},
{
"month": 12,
"positive": 455,
"total": 1765,
"year": 2020
},
{
"month": 1,
"positive": 270,
"total": 1264,
"year": 2021
},
{
"month": 2,
"positive": 82,
"total": 328,
"year": 2021
},
{
"month": 3,
"positive": 414,
"total": 1181,
"year": 2021
},
{
"month": 4,
"positive": 132,
"total": 420,
"year": 2021
},
{
"month": 5,
"positive": 182,
"total": 472,
"year": 2021
},
{
"month": 6,
"positive": 62,
"total": 182,
"year": 2021
},
{
"month": 7,
"positive": 207,
"total": 780,
"year": 2021
},
{
"month": 8,
"positive": 2587,
"total": 8381,
"year": 2021
},
{
"month": 9,
"positive": 764,
"total": 2395,
"year": 2021
},
{
"month": 10,
"positive": 178,
"total": 586,
"year": 2021
},
{
"month": 11,
"positive": 203,
"total": 937,
"year": 2021
},
{
"month": 12,
"positive": 99,
"total": 426,
"year": 2021
},
{
"month": 1,
"positive": 164,
"total": 576,
"year": 2022
},
{
"month": 2,
"positive": 113,
"total": 429,
"year": 2022
},
{
"month": 3,
"positive": 333,
"total": 970,
"year": 2022
},
{
"month": 4,
"positive": 130,
"total": 500,
"year": 2022
},
{
"month": 5,
"positive": 98,
"total": 345,
"year": 2022
},
{
"month": 6,
"positive": 301,
"total": 1443,
"year": 2022
},
{
"month": 7,
"positive": 911,
"total": 2484,
"year": 2022
},
{
"month": 8,
"positive": 176,
"total": 615,
"year": 2022
},
{
"month": 9,
"positive": 349,
"total": 1149,
"year": 2022
},
{
"month": 10,
"positive": 230,
"total": 961,
"year": 2022
},
{
"month": 11,
"positive": 188,
"total": 747,
"year": 2022
},
{
"month": 12,
"positive": 168,
"total": 863,
"year": 2022
},
{
"month": 1,
"positive": 246,
"total": 800,
"year": 2023
},
{
"month": 2,
"positive": 983,
"total": 4917,
"year": 2023
},
{
"month": 3,
"positive": 986,
"total": 4661,
"year": 2023
},
{
"month": 4,
"positive": 1427,
"total": 5601,
"year": 2023
},
{
"month": 5,
"positive": 342,
"total": 1728,
"year": 2023
},
{
"month": 6,
"positive": 805,
"total": 6001,
"year": 2023
},
{
"month": 7,
"positive": 642,
"total": 2609,
"year": 2023
},
{
"month": 8,
"positive": 1114,
"total": 5628,
"year": 2023
},
{
"month": 9,
"positive": 474,
"total": 2067,
"year": 2023
},
{
"month": 10,
"positive": 116,
"total": 512,
"year": 2023
},
{
"month": 11,
"positive": 359,
"total": 1219,
"year": 2023
},
{
"month": 12,
"positive": 321,
"total": 1047,
"year": 2023
},
{
"month": 1,
"positive": 641,
"total": 2731,
"year": 2024
},
{
"month": 2,
"positive": 222,
"total": 871,
"year": 2024
},
{
"month": 3,
"positive": 279,
"total": 1113,
"year": 2024
},
{
"month": 4,
"positive": 137,
"total": 675,
"year": 2024
},
{
"month": 5,
"positive": 682,
"total": 2965,
"year": 2024
},
{
"month": 6,
"positive": 990,
"total": 2908,
"year": 2024
},
{
"month": 7,
"positive": 1068,
"total": 3313,
"year": 2024
},
{
"month": 8,
"positive": 712,
"total": 2523,
"year": 2024
},
{
"month": 9,
"positive": 584,
"total": 1596,
"year": 2024
},
{
"month": 10,
"positive": 869,
"total": 2981,
"year": 2024
},
{
"month": 11,
"positive": 1474,
"total": 4965,
"year": 2024
}
]
```

### /bilibili/mpositive

```
[
{
"month": 1,
"positive": 1634,
"total": 6144
},
{
"month": 2,
"positive": 1796,
"total": 7650
},
{
"month": 3,
"positive": 2571,
"total": 11230
},
{
"month": 4,
"positive": 3585,
"total": 13291
},
{
"month": 5,
"positive": 2318,
"total": 8398
},
{
"month": 6,
"positive": 2602,
"total": 12277
},
{
"month": 7,
"positive": 3686,
"total": 12590
},
{
"month": 8,
"positive": 5607,
"total": 21187
},
{
"month": 9,
"positive": 2549,
"total": 9065
},
{
"month": 10,
"positive": 2338,
"total": 7984
},
{
"month": 11,
"positive": 2710,
"total": 9873
},
{
"month": 12,
"positive": 1399,
"total": 5457
}
]
```

### /xhs/ip

```
[
{
"heat_value": 1433873,
"region_name": "未知"
},
{
"heat_value": 55317,
"region_name": "云南"
},
{
"heat_value": 23252,
"region_name": "广东"
},
{
"heat_value": 9044,
"region_name": "河南"
},
{
"heat_value": 7152,
"region_name": "四川"
},
{
"heat_value": 5805,
"region_name": "美国"
},
{
"heat_value": 4675,
"region_name": "北京"
},
{
"heat_value": 3844,
"region_name": "浙江"
},
{
"heat_value": 3660,
"region_name": "江苏"
},
{
"heat_value": 2493,
"region_name": "山东"
},
{
"heat_value": 1716,
"region_name": "上海"
},
{
"heat_value": 1010,
"region_name": "陕西"
},
{
"heat_value": 647,
"region_name": "湖南"
},
{
"heat_value": 551,
"region_name": "中国香港"
},
{
"heat_value": 426,
"region_name": "福建"
},
{
"heat_value": 402,
"region_name": "天津"
},
{
"heat_value": 366,
"region_name": "河北"
},
{
"heat_value": 357,
"region_name": "重庆"
},
{
"heat_value": 321,
"region_name": "湖北"
},
{
"heat_value": 143,
"region_name": "宁夏"
},
{
"heat_value": 106,
"region_name": "安徽"
},
{
"heat_value": 96,
"region_name": "辽宁"
},
{
"heat_value": 80,
"region_name": "澳大利亚"
},
{
"heat_value": 66,
"region_name": "山西"
},
{
"heat_value": 59,
"region_name": "江西"
},
{
"heat_value": 38,
"region_name": "德国"
},
{
"heat_value": 35,
"region_name": "广西"
},
{
"heat_value": 32,
"region_name": "内蒙古"
},
{
"heat_value": 20,
"region_name": "黑龙江"
},
{
"heat_value": 18,
"region_name": "海南"
},
{
"heat_value": 12,
"region_name": "马来西亚"
},
{
"heat_value": 12,
"region_name": "加拿大"
},
{
"heat_value": 10,
"region_name": "新疆"
},
{
"heat_value": 8,
"region_name": "新加坡"
},
{
"heat_value": 8,
"region_name": "吉林"
},
{
"heat_value": 1,
"region_name": "甘肃"
},
{
"heat_value": 0,
"region_name": "中国台湾"
},
{
"heat_value": 0,
"region_name": "青海"
},
{
"heat_value": 0,
"region_name": "西班牙"
},
{
"heat_value": 0,
"region_name": "新西兰"
},
{
"heat_value": 0,
"region_name": "贵州"
},
{
"heat_value": 0,
"region_name": "意大利"
},
{
"heat_value": 0,
"region_name": "日本"
}
]
```



