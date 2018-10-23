Page({
  data: {
    menus: [{
      name: 'gcp状态',
      icon: '/assets/images/icon_tabbar.png',
      path: ''
    }, {
      name: '爬虫监控',
      icon: '/assets/images/icon_tabbar.png',
      path: '/pages/models/spider/index'
    }, {
      name: '下阶段计划',
      icon: '/assets/images/icon_tabbar.png',
      path: '/pages/models/next/index'
    }, {
      name: 'github',
      icon: '/assets/images/icon_tabbar.png',
      path: '/pages/models/github/index'
    }, {
      name: '关于我',
      icon: '/assets/images/icon_tabbar.png',
      path: ''
    }]
  },
  onLoad() {
  }
});