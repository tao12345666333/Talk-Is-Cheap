function getCookie(key) {
  const name = `${key}=`;
  const pair = document.cookie.split(';');

  for (let i = 0; i < pair.length; i++) {
    let item = pair[i];
    while (item.charAt(0) === ' ') item = item.substring(1);
    if (item.indexOf(name) === 0) return item.substring(name.length, item.length);
  }

  return '';
}

const Vue = require('vue');
const VueResource = require('vue-resource');

Vue.use(VueResource);

Vue.http.headers.common['X-CSRFTOKEN'] = getCookie('csrftoken');

const host = 'https://cnodejs.org';

exports.topic = {
  list(page, cb, eb) {
    Vue.http.get(`${host}/api/v1/topics?page=${page}`)
    .then(cb, eb);
  },
  detail(id, cb, eb) {
    const url = `${host}/api/v1/topic/${id}`;
    Vue.http.get(url).then(cb, eb);
  },
};

const localhost = '';

exports.tabset = {
  list(cb, eb) {
    Vue.http.get(`${localhost}/api/tab`)
    .then(cb, eb);
  },
};
