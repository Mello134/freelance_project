import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue';
// импорт представления /views/SignInView.vue
import SignInView from '../views/SignInView.vue';
// импорт представления /views/FirstComponentView.vue
import FirstComponentView from '../views/FirstComponentView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },
  // мой первый компонент
  {
    path: '/first',
    name: 'first',
    component: FirstComponentView,
  },
  // мой роутер для компонента SignIn и представления SignInView
  {
    path: '/auth/signin',
    name: 'signin',
    component: SignInView,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
