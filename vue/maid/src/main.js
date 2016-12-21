// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import VueRouter from 'vue-router';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';
import NProgress from 'nprogress';
import 'nprogress/nprogress.css';
import App from './App';
import Home from './views/Home';
import Task from './views/Task';
import TaskDetail from './views/TaskDetail';
import TaskList from './views/TaskList';


Vue.use(VueRouter);
Vue.use(ElementUI);

const routes = [{
  path: '/',
  component: Home,
  hidden: true,
}, {
  path: '/home',
  component: Home,
  name: 'A',
  iconCls: 'el-icon-message',
  children: [
    { path: '/g', component: Task, name: 'G' },
    { path: '/v', component: Task, name: 'V' },
    { path: '/p', component: Task, name: 'P' },
  ],
}, {
  path: '/home',
  component: Home,
  name: 'B',
  iconCls: 'el-icon-upload',
  children: [
    { path: '/online', component: Task, name: '上线' },
    { path: '/deploy', component: Task, name: '部署' },
  ],
}, {
  path: '/home',
  component: Home,
  name: 'C',
  iconCls: 'el-icon-setting',
  children: [
    { path: '/mysql', component: Task, name: 'MySQL' },
    { path: '/redis', component: Task, name: 'Redis' },
    { path: '/backup', component: Task, name: '备份' },
    { path: '/sqlreview', component: Task, name: 'SQL' },
  ],
}, {
  path: '/tasks',
  component: Home,
  hidden: true,
  children: [
    { path: 'all', component: TaskList, name: '所有任务' },
    { path: 'ready', component: TaskList, name: '未开始' },
    { path: 'running', component: TaskList, name: '进行中' },
    { path: 'finish', component: TaskList, name: '已完成' },
    { path: 'detail', component: TaskDetail, name: '详细' },
  ],
},
];

const router = new VueRouter({
  routes,
});


router.beforeEach((to, from, next) => {
  NProgress.start();
  next();
});

// router.afterEach(transition => {
router.afterEach(() => {
  NProgress.done();
});

/* eslint-disable no-new */
/*
new Vue({
  el: '#app',
  router,
  ...App,
});

*/

new Vue({
  el: '#app',
  template: '<App/>',
  router,
  components: { App },
}).$mount('#app');
