// index.js
import F2 from '../../../libs/f2-canvas/lib/f2';

let chart = null;

function initChart(canvas, width, height) { // 使用 F2 绘制图表
  const data = [
    { time: '11:00', rate: 38 },
    { time: '12:00', rate: 52 },
    { time: '13:00', rate: 61 },
    { time: '14:00', rate: 145 },
    { time: '15:00', rate: 48 },
  ];
  chart = new F2.Chart({
    el: canvas,
    width,
    height
  });
  chart.source(data);
  chart.tooltip({
    showItemMarker: false,
    onShow(ev) {
      console.log(ev)
      const { items } = ev;
      items[0].name = items[0].title;
      items[0].value = items[0].value + 't/h';
    }
  });
  chart.interval().position('time*rate');
  chart.render();
  return chart;
}

Page({
  data: {
    opts: {
      onInit: initChart
    },
    spiderList: [{
      id: 'x342',
      name: '当当爬虫',
      status: 'working'
    }, {
      id: 'j432',
      name: '京东爬虫',
      status: 'working'
    }]
  },
  onLoad: function (options) {
   
  }
})