import Vue from 'vue';
import Router from 'vue-router';
import Main from '@/views/Main';
import Login from '@/views/Login';
import Index from '@/views/Index';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/main',
      name: 'Main',
      component: Main,
      children: [
        {
          path: '/',
          name: 'Index',
          component: Index,
        },
      ],
    },
  ],
});
