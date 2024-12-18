//中国地图


(function(){
    var myChart =echarts.init(document.querySelector(".map .chart"));
    
    
    
    
var  option = {
      title: {
          text: '地区热度分布',
          subtext: '',
          left: 'center',
          textStyle:{
            color:'#ffeb7b'
          }
          
      },
      tooltip: {
          trigger: 'item'
      },
      legend: {
          orient: 'vertical',
          left: 'left',
          data:['小红书','知乎','Bilibili'],
          textStyle:{
            color:'ffffff'
          }
      },
      visualMap: {
          min: 0,
          max: 8500,
          left: 'left',
          top: 'bottom',
          text: ['高','低'],           // 文本，默认为数值文本
          calculable: true,
          inRange:{
            color: ['#D7CEFF', '#62393c']
          },
          outOfRange:{
            color:['#D7CEFF']
          }
      },
      toolbox: {
          show: true,
          orient: 'vertical',
          left: 'right',
          top: 'center',
          feature: {
              /* dataView: {readOnly: false}, */
              restore: {},
              saveAsImage: {}
          }
      },
      series: [
          {
              name: '小红书',
              type: 'map',
              mapType: 'china',
              roam: false,
              label: {
                  normal: {
                      show: true
                  },
                  emphasis: {
                      show: true
                  }
              },
              data:[]
          },
          {
              name: '知乎',
              type: 'map',
              mapType: 'china',
              label: {
                  normal: {
                      show: true
                  },
                  emphasis: {
                      show: true
                  }
              },
              data:[

              ]
          },
          {
              name: 'Bilibili',
              type: 'map',
              mapType: 'china',
              label: {
                  normal: {
                      show: true
                  },
                  emphasis: {
                      show: true
                  }
              },
              data:[]
          }
      ]
    };
    
    // 用于动态更新系列数据的方法
    function updateSeriesData(data, seriesIndex) {
        var newData = [];
        data.forEach(item => {
            newData.push({ name: item.region_name, value: item.heat_value });
        });
        option.series[seriesIndex].data = newData;
    }
    
    /*json的格式，改参数名字无所谓 
    [
        { "region_name": "北京", "heat_value": 1000 },
        { "region_name": "上海", "heat_value": 800 },
        { "region_name": "广东", "heat_value": 1200 }
    ]
     */
    
    
    // 接口请求，分别获取小红书、知乎和Bilibili数据，获取不成功不会变化
    $.ajax({
        url: "http://localhost:8088/xhs/ip", // 小红书接口地址
        type: "GET",
        success: function (data) {
            updateSeriesData(data, 0); // 更新第一个系列（小红书）
            myChart.setOption(option);
        }
    });
    
    $.ajax({
        url: "http://localhost:8088/zhihu/ip", // 知乎接口地址
        type: "GET",
        success: function (data) {
            updateSeriesData(data, 1); // 更新第二个系列（知乎）
            myChart.setOption(option);
        }
    });

      myChart.setOption(option);
    })();