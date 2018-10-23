import configs from '../../../settings/configs.js';

Page({
  data: {
    repositoryList: []
  },
  onLoad: function(options) {
    let self = this;

    wx.request({
      url: configs.getUrl + '/github',
      data: {
        x: '123',
      },
      success(res) {
        self.setData({
          repositoryList: res.data
        })
      }
    })
  },
})