var IP = window.location.host;




var init_echart = function() {
    let data_len = 20;
    // var x_data = new Array(data_len), i=x_data.length;
    // while(i--){x_data[i] = '';}
    var y_data = new Array(data_len), i=y_data.length;
    while(i--){y_data[i] = 0;}
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('main'));
    // 指定图表的配置项和数据
    option = {
        xAxis: {
            type: 'category',
            boundaryGap: false,
            // data: x_data
        },
        yAxis: {
            type: 'value',
            scale:true,
            min: function(value) {
                return value.min - 20;
            } // value 包含最小值value.min
        },
        series: [{
            data: y_data,
            type: 'line',
            areaStyle: {},
            symbol:'none',  //这句就是去掉点的  
            smooth:true,  //这句就是让曲线变平滑的 
            // itemStyle : { normal: {label : {show: true}}}
        }]
    };


    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}

var set_echart = function(data) {
    var myChart = echarts.init(document.getElementById('main'));
    // 显示标题，图例和空的坐标轴
    let new_value = data['AIVal'][0]["Val"];
    let data_array = get_old_data(myChart);
    set_data(data_array, new_value);

    option = {series: {data: data_array}};
    myChart.setOption(option);
}

var get_old_data = function(echat) {
    return echat.getOption().series[0].data;
}

var set_data = function(data, new_value) {
    data.splice(0, 1,);
    data.splice(data.length, 1, new_value);
}

var lamp_change = function(e, choose) {
    let url;
    if (choose == 1) {
        url = 'http://' + IP + '/lamp1_change';
    } else {
        url = 'http://' + IP + '/lamp2_change'
    }
    axios.get(url)
      .then(function (response) {
        set_lamp();
      })
      .catch(function (error) {
        console.log(error);
    });
}

var lamp1_change = function(e) {
    // 可选地，上面的请求可以这样做
    lamp_change(e, 1);
}

var lamp2_change = function(e) {
    // 可选地，上面的请求可以这样做
    lamp_change(e, 2);
}

var lamp_state = function() {
    // 可选地，上面的请求可以这样做
    axios.get('http://' + IP + '/lamp_get')
      .then(function (response) {
        let res = response.data;
        let state = {
            lamp1: res["DOVal"][0]["Val"],
            lamp2: res["DOVal"][1]["Val"],
        };
        set_lamp(state);
      })
      .catch(function (error) {
        console.log(error);
      });
}

var set_lamp = function(state) {

    let _set_lamp = function(_e, _state) {
        if (_state == 0) {
            _e.checked = '';
        } else {
            _e.checked = 'checked';
        }
    }

    let lamp1 = document.getElementById('lamp1');
    let lamp2 = document.getElementById('lamp2');
    _set_lamp(lamp1, state['lamp1']);
    _set_lamp(lamp2, state['lamp2']);
}

var ai_lamp = function() {
    axios.get('http://' + IP + '/ai_info')
      .then(function (response) {
        set_echart(response.data);
      })
      .catch(function (error) {
        console.log(error);
      }
    );
}