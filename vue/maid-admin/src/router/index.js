import Vue from 'vue';
import Router from 'vue-router';
import Main from '@/views/Main';
import Login from '@/views/Login';
import Index from '@/views/Index';
import Process from '@/views/Process';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
    },
    {
      path: '/main',
      name: 'Main',
      component: Main,
      children: [
        {
          path: 'process',
          name: 'Process',
          component: Process,
        },
        {
          path: 'index',
          name: 'Index',
          component: Index,
        },
      ],
    },
  ],
});
