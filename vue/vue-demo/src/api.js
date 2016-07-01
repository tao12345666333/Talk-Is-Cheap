const Vue = require('vue');
const VueResource = require('vue-resource');

Vue.use(VueResource);

exports.topic = {
  list: function (cb, eb) {
    Vue.http.get('http://cnodejs.org/api/v1/topics').then(cb, eb);
  },
};
