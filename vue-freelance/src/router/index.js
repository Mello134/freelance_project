import Vue from 'vue';
import VueRouter from 'vue-router';

/* Импорт компонентов */
// импорт компонента /components/auth/SignIn.vue and SignUp.vue
import SignIn from '@/components/auth/SignIn.vue';
import SignUp from '@/components/auth/SignUp.vue';

/* Импорт представлений */
import HomeView from '../views/HomeView.vue';
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
  // мои роутеры для компонентов SignIn и SignUp
  {
    path: '/auth/signin',
    name: 'SignIn',
    component: SignIn,
  },
  {
    path: '/auth/signup',
    name: 'SignUp',
    component: SignUp,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
