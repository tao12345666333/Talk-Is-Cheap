import Vue from 'vue';
import VueRouter from 'vue-router';

import Mark from './components/Mark';

Vue.use(VueRouter);

const router = new VueRouter();

router.map({
  '/': {
    name: 'mark',
    component: Mark,
  },
});

const App = require('./App.vue');

router.start(App, 'app');
