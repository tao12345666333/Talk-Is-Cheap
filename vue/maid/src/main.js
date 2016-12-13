// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import VueRouter from 'vue-router';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';
import App from './App';
import Home from './components/Home';

Vue.use(VueRouter);
Vue.use(ElementUI);

const routes = [{
  path: '/',
  component: Home,
}, {
  path: '/home',
  component: Home,
}];

const router = new VueRouter({
  routes,
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  ...App,
});
