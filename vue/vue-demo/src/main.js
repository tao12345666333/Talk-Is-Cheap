import Vue from 'vue';
import VueRouter from 'vue-router';

import Mark from './components/Mark';
import permission from './views/permission';

Vue.use(VueRouter);

const router = new VueRouter();

router.map({
  '/': {
    name: 'mark',
    component: Mark,
  },
  '/foo': {
    name: 'permission',
    component: permission,
  },
});

const App = require('./App.vue');

router.start(App, 'app');
