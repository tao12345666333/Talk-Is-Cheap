const Vue = require('vue');
const VueResource = require('vue-resource');

Vue.use(VueResource);

exports.topic = {
  list(page, cb, eb) {
    Vue.http.get(`http://cnodejs.org/api/v1/topics?page=${page}`).then(cb, eb);
  },
  detail(id, cb, eb) {
    const url = `http://cnodejs.org/api/v1/${id}`;
    Vue.http.get(url).then(cb, eb);
  },
};
