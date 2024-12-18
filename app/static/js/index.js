//显示时间
(function(){
  var t = null;
  t = setTimeout(time, 1000); //開始运行
  function time() {
    clearTimeout(t); //清除定时器
    dt = new Date();
    var y = dt.getFullYear();
    var mt = dt.getMonth() + 1;
    var day = dt.getDate();
    var h = dt.getHours(); //获取时
    var m = dt.getMinutes(); //获取分
    var s = dt.getSeconds(); //获取秒
    document.querySelector(".showTime").innerHTML =
      "当前时间：" +
      y +
      "年" +
      mt +
      "月" +
      day +
      "日-" +
      h +
      "时" +
      m +
      "分" +
      s +
      "秒";
    t = setTimeout(time, 1000); //设定定时器，循环运行
  }
})();





//最上边那俩数字
//这个是帖子数+视频数
(function(){
  // 函数用于获取数据
  function fetchDataAndReplace() {
    // 三个平台接口
    var platforms = ["xhs", "zhihu", "bilibili"];
    var totalCount = 0;

    // 遍历平台，调用接口
    platforms.forEach(function (platform, index) {
      $.ajax({
        url: `http://localhost:8088/${platform}/count`, // 替换为实际接口路径
        type: "GET",
        success: function (data) {
          // 假设接口返回的数据格式如下：
          // { "count": 12345 }
          // console.log(data);
          totalCount += data.count;

          // 当所有接口请求完成后更新页面
          if (index === platforms.length - 1) {
            updateTotalCount(totalCount);
          }
        },
        error: function () {
          console.error(`Error fetching data from ${platform}`);
          // 即使请求失败，仍然在最后一次更新
          if (index === platforms.length - 1) {
            updateTotalCount(totalCount);
          }
        }
      });
    });
  }

  // 函数用于更新 <li> 内容
  function updateTotalCount(total) {
    document.getElementById("totalCount1").innerText = total;
  }

  // 调用函数获取数据并更新页面
  fetchDataAndReplace();
})();


//这个是评论总数
(function(){
  // 函数用于获取数据
  function fetchDataAndReplace() {
    // 三个平台接口
    var platforms = ["xhs", "zhihu", "bilibili"];
    var totalCount = 0;

    // 遍历平台，调用接口
    platforms.forEach(function (platform, index) {
      $.ajax({
        url: `http://localhost:8088/${platform}/comment`, // 替换为实际接口路径
        type: "GET",
        success: function (data) {
          // 假设接口返回的数据格式如下：
          // { "count": 12345 }
          // console.log(data);
          totalCount += parseInt(data.count,10);

          // 当所有接口请求完成后更新页面
          if (index === platforms.length - 1) {
            updateTotalCount(totalCount);
          }
        },
        error: function () {
          console.error(`Error fetching data from ${platform}`);
          // 即使请求失败，仍然在最后一次更新
          if (index === platforms.length - 1) {
            updateTotalCount(totalCount);
          }
        }
      });
    });
  }

  // 函数用于更新 <li> 内容
  function updateTotalCount(total) {
    document.getElementById("totalCount2").innerText = total;
  }

  // 调用函数获取数据并更新页面
  fetchDataAndReplace();
})();








// 柱状图1模块-热度排布--热度最高的五个帖子||话题
(function() {
  // 实例化对象
  var myChart = echarts.init(document.querySelector(".bar .chart"));
  // 指定配置和数据
  var option = {
    color: ["#2f89cf"],
    tooltip: {
      trigger: "axis",
      axisPointer: {
        // 坐标轴指示器，坐标轴触发有效
        type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    grid: {
      left: "0%",
      top: "10px",
      right: "0%",
      bottom: "4%",
      containLabel: true
    },
    xAxis: [
      {
        type: "category",
        data: [],
        axisTick: {
          alignWithLabel: true
        },
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        },
        axisLine: {
          show: false
        }
      }
    ],
    yAxis: [
      {
        type: "value",
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        },
        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        }
      }
    ],
    series: [
      {
        name: "热度",
        type: "bar",
        barWidth: "35%",
        data: [],
        itemStyle: {
          barBorderRadius: 5
        }
      }
    ]
  };

  // 把配置给实例对象
  myChart.setOption(option);
  window.addEventListener("resize", function() {
    myChart.resize();
  });

  // 数据容器（初始）可删
  var dataAll = [
    {
      year: "小红书",
      data: [1058788, 72373.5, 53100.5, 27500, 23684],
      xAxis: [
        "网络暴力我们该如何自救，希望你们永远遇不到",
        "帮主播怼赢键盘侠",
        "发疯后续·妈妈视奸，被“网络暴力”气哭了",
        "最近我注意到了这类网络现象，所以画了下来。",
        "如果你被网暴了，请你这样做??"
      ] // 对应的 xAxis 数据
    },
    {
      year: "知乎",
      data: [22015, 21201, 19044.5, 12664, 12562],
      xAxis: [
        "成都大学党委书记毛洪涛遗体已被找到，案件还有哪些值得关注的信息？",
        "你见过的男生，可以有多坏？",
        "14岁少女被键盘侠逼死，父亲邀请凶手参加葬礼：网络暴力有多可怕？",
        "如何评价中国政法大学罗翔教授？",
        "对蔡徐坤的黑是否过度已构成网络暴力？"
      ]
    },
    {
      year: "Bilibili",
      data: [29229955, 11511422, 13519396.5, 11395927, 10316862.5],
      xAxis: [
          "被“实锤”家暴、视频造假将近一年，我是怎么回应的？",
          "【罗翔】聊聊网络喷子与键盘侠", 
          "还原一下著名的《潘博文事件》",
          "触目惊心！缅北诈骗集团内部视频流出。。。", 
            "究竟网络暴力带来了什么？"
          ]
    }
  ];

    // 数据获取函数
    function fetchData() {
        // 从三个接口分别获取数据
        $.ajax({
            url: "http://localhost:8088/xhs/heat", // 替换为实际的接口地址
            type: "GET",
            success: function (data) {
                handleData(data, "小红书");
            }
        });

        $.ajax({
            url: "http://localhost:8088/zhihu/heat", // 替换为实际的接口地址
            type: "GET",
            success: function (data) {
                handleData(data, "知乎");
            }
        });

        $.ajax({
            url: "http://localhost:8088/bilibili/heat", // 替换为实际的接口地址
            type: "GET",
            success: function (data) {
                handleData(data, "Bilibili");
            }
        });
    }

    // 处理数据函数
  function handleData(data, platform) {
    var topData = data.slice(0, 5);
    var names = topData.map(item => item.content);
    var values = topData.map(item => item.heat);

    // 更新 dataAll 的内容
    dataAll.forEach(item => {
      if (item.year === platform) {
        item.data = values;
        item.xAxis = names;
      }
    });

    // 默认显示小红书的数据
    if (platform === "小红书") {
      option.series[0].data = values;
      option.xAxis[0].data = names;
      myChart.setOption(option);
    }
  }



  // 点击切换数据
  $(".bar h2").on("click", "a", function() {
    var index = $(this).index();
    option.series[0].data = dataAll[index].data; // 切换数据
    option.xAxis[0].data = dataAll[index].xAxis; // 切换 xAxis 数据
    myChart.setOption(option);
  });

  fetchData();
  

})();






// 折线图--热度变化
(function () {
  // 基于准备好的dom，初始化echarts实例
  var myChart = echarts.init(document.querySelector(".line .chart"));

  // 初始化配置选项
  const colorList = ["#9E87FF", "#73DDFF", "#fe9a8b"];
  var option = {
    color: colorList,
    title: {
      textStyle: {
        fontSize: 12,
        fontWeight: 400,
      },
      left: "center",
      top: "5%",
    },
    legend: {
      icon: "circle",
      top: "5%",
      right: "5%",
      itemWidth: 6,
      itemGap: 20,
      textStyle: {
        color: "#556677",
      },
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        label: {
          show: true,
          backgroundColor: "#fff",
          color: "#556677",
        },
      },
      backgroundColor: "#fff",
      textStyle: {
        color: "#5c6c7c",
      },
      padding: [10, 10],
      extraCssText: "box-shadow: 1px 0 2px 0 rgba(163,163,163,0.5)",
    },
    grid: {
      top: "15%",
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true,
    },
    xAxis: {
      type: "category",
      boundaryGap: false,
      data: [],
      axisLine: {
        lineStyle: {
          color: "#DCE2E8",
        },
      },
      axisTick: {
        show: false,
      },
      axisLabel: {
        textStyle: {
          color: "#556677",
        },
        fontSize: 12,
        margin: 15,
      },
    },
    yAxis: {
      type: "value",
      axisTick: {
        show: false,
      },
      axisLine: {
        lineStyle: {
          color: "#DCE2E8",
        },
      },
      axisLabel: {
        textStyle: {
          color: "#556677",
        },
      },
      splitLine: {
        show: false,
      },
    },
    series: [
      {
        name: "小红书",
        type: "line",
        smooth: true,
        data: [],
        lineStyle: {
          width: 5,
          color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
            { offset: 0, color: "#9effff" },
            { offset: 1, color: colorList[0] },
          ]),
        },
        itemStyle: {
          color: colorList[0],
        },
      },
      {
        name: "知乎",
        type: "line",
        smooth: true,
        data: [],
        lineStyle: {
          width: 5,
          color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
            { offset: 0, color: "#73DD39" },
            { offset: 1, color: colorList[1] },
          ]),
        },
        itemStyle: {
          color: colorList[1],
        },
      },
      {
        name: "Bilibili",
        type: "line",
        smooth: true,
        data: [],
        lineStyle: {
          width: 5,
          color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
            { offset: 0, color: "#fe9a" },
            { offset: 1, color: colorList[2] },
          ]),
        },
        itemStyle: {
          color: colorList[2],
        },
      },
    ],
  };

  // 重新配置选项
  myChart.setOption(option);

  // 数据获取与更新函数
  function fetchData() {
    const apiEndpoints = [
      { url: "http://localhost:8088/xhs/mheating", name: "小红书" },
      { url: "http://localhost:8088/zhihu/mheating", name: "知乎" },
      { url: "http://localhost:8088/bilibili/mheating", name: "Bilibili" },
    ];

    let xAxisData = [];
    let seriesData = [[], [], []];

    apiEndpoints.forEach((endpoint, index) => {
      $.ajax({
        url: endpoint.url,
        type: "GET",
        success: function (data) {
          processData(data, index, xAxisData, seriesData, endpoint.name);
        },
      });
    });

    function processData(data, index, xAxisData, seriesData, platform) {
      const months = data.map((item) => `${item.month}月`);
      const values = data.map((item) => parseFloat(item.total_heat));

      if (xAxisData.length === 0) xAxisData.push(...months);
      seriesData[index] = values;

      if (seriesData.every((data) => data.length > 0)) {
        updateChart(xAxisData, seriesData);
      }
    }
  }

  // 更新图表函数
  function updateChart(xAxisData, seriesData) {
    option.xAxis.data = xAxisData;
    option.series.forEach((series, index) => {
      series.data = seriesData[index];
    });
    myChart.setOption(option);
  }

  // 初始化数据获取
  fetchData();

  // 响应式处理
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();




// 饼形图定制--情感占比
(function() {
  // 基于准备好的dom，初始化echarts实例
  var myChart = echarts.init(document.querySelector(".pie .chart"));

var  option = {
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b}: {c} ({d}%)",
      position: function(p) {
        //其中p为当前鼠标的位置
        return [p[0] + 10, p[1] - 10];
      }
    },
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      data: ["正向", "负向"],
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    series: [
      {
        name: "情感占比",
        type: "pie",
        center: ["50%", "42%"],
        radius: ["40%", "60%"],
        color: [
          "#bf444c",
          "#066eab",
          "#0682ab",
          "#0696ab",
          "#06a0ab",
          "#06b4ab",
          "#06c8ab",
          "#06dcab",
          "#06f0ab"
        ],
        label: { show: false },
        labelLine: { show: false },
        data: [
          { value: 36853, name: "正面" },
          { value: 104798, name: "负面" },
        ]
      }
    ]
  };

  // 使用刚指定的配置项和数据显示图表。
  myChart.setOption(option);
  window.addEventListener("resize", function() {
    myChart.resize();
  });

// 获取数据的函数
  function fetchData() {
    // 三个平台数据
    var platforms = ["xhs", "zhihu", "bilibili"];
    var seriesSum = {}; // 中间对象，用于累加数据

    // 遍历平台，调用接口
    platforms.forEach(function (platform, index) {
      $.ajax({
        url: `http://localhost:8088/${platform}/total`, // 替换为实际接口路径
        type: "GET",
        success: function (data) {
          // 累加 series 数据
          data.series.forEach(function (item) {
            if (!seriesSum[item.name]) {
              seriesSum[item.name] = 0;
            }
            seriesSum[item.name] += item.value;
          });

          // 更新图表（所有请求完成后）
          if (index === platforms.length - 1) {
            var seriesData = Object.keys(seriesSum).map(function (key) {
              return { name: key, value: seriesSum[key] };
            });
            updateChart(seriesData);
          }
        }
      });
    });
  }

  // 更新图表
  function updateChart(seriesData) {
    // 从 seriesData 中提取 legend 数据
    var legendData = seriesData.map(function (item) {
      return item.name;
    });
    option.legend.data = Array.from(new Set(legendData)); // 去重
    option.series[0].data = seriesData;
    myChart.setOption(option);
  }

  // 调用获取数据函数
  fetchData();


})();




//轮播图--词云图
(function(){
  const images = [
    '/static/images/bilibili.png',
    '/static/images/xhs.png',
    '/static/images/zhihu.png'
  ];

  const slideshow = document.querySelector('.slideshow');
  let currentIndex = 0;

  function changeImage() {
    slideshow.style.backgroundImage = `url(${images[currentIndex]})`;
    currentIndex = (currentIndex + 1) % images.length;
  }   
  changeImage();

  setInterval(changeImage, 4000);

})();







// 折线图 情感占比变化
(function() {
  // 基于准备好的dom，初始化echarts实例
  var myChart = echarts.init(document.querySelector(".line1 .chart"));
  var option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        lineStyle: {
          color: "#dddc6b"
        }
      }
    },
    legend: {
      top: "0%",
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    grid: {
      left: "10",
      top: "30",
      right: "10",
      bottom: "10",
      containLabel: true
    },

    xAxis: [
      {
        type: "category",
        boundaryGap: false,
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12
          }
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.2)"
          }
        },

        data: [
          "01","02","03","04","05","06","07","08","09","11","12"
        ]
      },
      {
        axisPointer: { show: false },
        axisLine: { show: false },
        position: "bottom",
        offset: 20
      }
    ],

    yAxis: [
      {
        type: "value",
        axisTick: { show: false },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        },
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12
          }
        },

        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        }
      }
    ],
    series: [
      {
        name: "小红书",
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 5,
        showSymbol: false,
        lineStyle: {
          normal: {
            color: "#0184d5",
            width: 2
          }
        },
        areaStyle: {
          normal: {
            color: new echarts.graphic.LinearGradient(
              0,0,0,1,
              [
                {
                  offset: 0,
                  color: "rgba(1, 132, 213, 0.4)"
                },
                {
                  offset: 0.8,
                  color: "rgba(1, 132, 213, 0.1)"
                }
              ],
              false
            ),
            shadowColor: "rgba(0, 0, 0, 0.1)"
          }
        },
        itemStyle: {
          normal: {
            color: "#0184d5",
            borderColor: "rgba(221, 220, 107, .1)",
            borderWidth: 12
          }
        },
        data: [
          0.1333333333,0.1147540984,0.2222222222,0.1538461538,0.1955128205,0.1307189542,0.1451612903,0.2364341085,0.2571428571,0.1993127148,0.1842105263,0.2631578947
          ]
      },
      {
        name: "知乎",
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 5,
        showSymbol: false,
        lineStyle: {
          normal: {
            color: "#00d887",
            width: 2
          }
        },
        areaStyle: {
          normal: {
            color: new echarts.graphic.LinearGradient(
              0,
              0,
              0,
              1,
              [
                {
                  offset: 0,
                  color: "rgba(0, 216, 135, 0.4)"
                },
                {
                  offset: 0.8,
                  color: "rgba(0, 216, 135, 0.1)"
                }
              ],
              false
            ),
            shadowColor: "rgba(0, 0, 0, 0.1)"
          }
        },
        itemStyle: {
          normal: {
            color: "#00d887",
            borderColor: "rgba(221, 220, 107, .1)",
            borderWidth: 12
          }
        },
        data: [
          0.1962962963,
          0.2036199095,
          0.2826086957,
          0.2011494253,
          0.2324723247,
          0.1861702128,
          0.2213114754,
          0.2076271186,
          0.1744186047,
          0.3492063492,
          0.2631578947,
          0.2631578947
        ]
      },
      {
        name: "Bilibili",
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 5,
        showSymbol: false,
        lineStyle: {
          normal: {
            color: "#e06c75",
            width: 2
          }
        },
        areaStyle: {
          normal: {
            color: new echarts.graphic.LinearGradient(
              0,
              0,
              0,
              1,
              [
                {
                  offset: 0,
                  color: "rgba(0, 216, 135, 0.4)"
                },
                {
                  offset: 0.8,
                  color: "rgba(0, 216, 135, 0.1)"
                }
              ],
              false
            ),
            shadowColor: "rgba(0, 0, 0, 0.1)"
          }
        },
        itemStyle: {
          normal: {
            color: "#e06c75",
            borderColor: "rgba(221, 220, 107, .1)",
            borderWidth: 12
          }
        },
        data: [
          0.2687407407,
          0.2366403209,
          0.2256633533,
          0.2706916684,
          0.2761583642,
          0.2159951984,
          0.2867530598,
          0.2645604986,
          0.2794452888,
          0.2884308813,
          0.2742345737,
          0.2560815253
        ]
      }
    ]
  };

  // 使用刚指定的配置项和数据显示图表。
  myChart.setOption(option);
  window.addEventListener("resize", function() {
    myChart.resize();
  });




// 动态获取数据并更新图表
function fetchDataAndUpdate() {
  var platforms = ["xhs", "zhihu", "bilibili"];
  var seriesData = [[], [], []]; // 存储各平台的情感占比数据
  var xAxisData = []; // 存储月份数据

  platforms.forEach(function (platform, index) {
    $.ajax({
      url: `http://localhost:8088/${platform}/mpositive`, // 替换为实际接口路径
      type: "GET",
      dataType: "json",
      success: function (response) {
        // 假设接口返回的数据格式为：
        // [
        //   { "month": 1, "positive": 1634, "total": 6144 },
        //   { "month": 2, "positive": 1796, "total": 7650 },
        //   ...
        // ]
        // 按月提取情感占比数据
        response.forEach(function (item) {
          if (xAxisData.length < response.length) {
            // 动态设置 x 轴数据（月份）
            xAxisData.push(`${item.month}月`);
          }

          // 计算正面情感百分比
          seriesData[index].push(item.total === 0 ? 0 : (item.positive / item.total) );
        });

        // 确保所有数据获取完毕后更新图表
        if (seriesData.every((arr) => arr.length > 0)) {
          option.xAxis.data = xAxisData; // 设置 x 轴月份
          option.series[0].data = seriesData[0]; // 小红书
          option.series[1].data = seriesData[1]; // 知乎
          option.series[2].data = seriesData[2]; // Bilibili
          // 更新图表
          myChart.setOption(option);
        }
      },
      error: function (xhr, status, error) {
        console.error(`Error fetching data for ${platform}:`, error);
      },
    });
  });
}

fetchDataAndUpdate();

})();






// 时间段分布统计模块
(function() {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".pie1  .chart"));
  // 2. 指定配置项和数据
  var option = {
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    // 注意颜色写的位置
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      
    ],
    series: [
      {
        name: "占比统计",
        type: "pie",
        // 如果radius是百分比则必须加引号
        radius: ["10%", "70%"],
        center: ["50%", "42%"],
        roseType: "radius",
        data: [],
        // 修饰饼形图文字相关的样式 label对象
        label: {
          fontSize: 10
        },
        // 修饰引导线样式
        labelLine: {
          // 连接到图形的线长度
          length: 10,
          // 连接到文字的线长度
          length2: 10
        }
      }
    ]
  };

  
  //接口
  // 数据容器
  var summaryData = {
    "上午": 0,
    "下午": 0,
    "晚上": 0,
    "凌晨": 0
};

// 数据处理函数
function processData(data) {
    data.forEach(item => {
        if (summaryData[item.time_period] !== undefined) {
            summaryData[item.time_period] += item.value;
        }
    });
}

// 更新图表数据
function updateChart() {
    var seriesData = Object.keys(summaryData).map(key => ({
        name: key,
        value: summaryData[key]
    }));
    option.series[0].data = seriesData;
    myChart.setOption(option);
}

// AJAX 请求
function fetchData() {
    $.ajax({
        url: "http://localhost:8088/xhs/time", // 小红书接口
        type: "GET",
        success: function (data) {
            processData(data);
            updateChart();
        }
    });

    $.ajax({
        url: "http://localhost:8088/zhihu/time", // 知乎接口
        type: "GET",
        success: function (data) {
            processData(data);
            updateChart();
        }
    });

    $.ajax({
        url: "http://localhost:8088/bilibili/time", // Bilibili接口
        type: "GET",
        success: function (data) {
            processData(data);
            updateChart();
        }
    });
}

/* json格式
[
    { "time_period": "早上", "value": 10 },
    { "time_period": "下午", "value": 20 },
    { "time_period": "晚上", "value": 15 },
    { "time_period": "凌晨", "value": 5 }
] */

  
  // 3. 配置项和数据给我们的实例化对象
  myChart.setOption(option);
  fetchData();
  // 4. 当我们浏览器缩放的时候，图表也等比例缩放
  window.addEventListener("resize", function() {
    // 让我们的图表调用 resize这个方法
    myChart.resize();
  });
})();


