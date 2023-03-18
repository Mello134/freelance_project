import Vue from 'vue';

/* регистрирую все модули и плагины */
// axios
import axios from 'axios';
import VueAxios from 'vue-axios';
// BootstrapVue
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

/* плагины установленные в начале vue create vue-freelance */
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;
/* модули и плагины доступные для всего проекта */
// axios
Vue.use(VueAxios, axios);
// BootstrapVue
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
// Vue.use(router) ????????????????????

new Vue({
  router,
  render: (h) => h(App),
  axios,
}).$mount('#app');
