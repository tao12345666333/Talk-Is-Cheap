import Vue from 'vue';
import VueRouter from 'vue-router';

import Mark from './components/Mark';
import topic from './views/topic';

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
});

const App = require('./App.vue');

router.start(App, 'app');
