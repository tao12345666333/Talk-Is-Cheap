Page({
  data: {
    moes: []
  },
  onLoad: function () {
    this.setData({
      moes: [
          {
              name: 'TaoBeier',
              title: '利器系列-更高效的Vim',
              time: '9月24日',
              intro: '一份开箱即用的的高效Vim配置，对VimVim 8也完美适用. http://moelove.info/vim',
              content: '请到 http://github.com/tao12345666333/vim 使用',
              banner: 'https://pic4.zhimg.com/409f4c6f6b7230d4e9d48a9ca015fdab_b.png'
          }
      ]
    })
  }
})