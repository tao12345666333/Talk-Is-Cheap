import Vue from 'vue';
import VueRouter from 'vue-router';

import Mark from './components/Mark';
import topic from './views/topic';
import topics from './views/topics';
import topicItem from './views/topicItem';
import Bar from './views/Bar';

Vue.component('mark', Mark);
Vue.component('topic', topic);
Vue.component('topics', topics);
Vue.component('topic-item', topicItem);
Vue.component('bar', Bar);

Vue.use(VueRouter);

const router = new VueRouter();

router.map({
  '/': {
    name: 'mark',
    component: Mark,
  },
  '/foo': {
    name: 'topic',
    component: topic,
  },
  '/foos/:pageNum': {
    name: 'topics',
    component: topics,
  },
  '/foo/:topic_id': {
    name: 'detail',
    component: topicItem,
  },
  '/bar': {
    name: 'bar',
    component: Bar,
  },
});

const App = require('./App.vue');

router.start(App, 'app');
