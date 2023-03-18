<!-- eslint-disable vuejs-accessibility/label-has-for -->
<template>
  <div class="w-50 mx-auto border p-2 m-3 rounded">
    <b-form @submit="login">
      <div class="form-group p-2">
        <label for="username">Логин:</label>
        <b-input v-model="username" type="text" id="username" placeholder="Логин.."></b-input>
      </div>
      <div class="form-group p-2">
        <label for="password">Пароль:</label>
        <b-input v-model="password" type="password" id="password" placeholder="Пароль.."></b-input>
      </div>
      <b-button variant="primary" type="submit" class="mx-2">Войти</b-button>
      <p class="mt-3">
        Ещё не зарегестрированы?
        <router-link to="/auth/signup">Регистрация</router-link>
      </p>
    </b-form>
  </div>
</template>

<script>
/* разрешаю экспорт этого компонента {
  имя_компонента,
  данные_компонента() {
    возврашаем {
      логин: изначально пустой,
      пароль: изначально пустой,
    };
  },
  методы: {
    событие_логин(эвент) {
      обработчик события= останавливаю событие;
      логика авторизации
    },
    событие_вход(токен) {
      токен, в консоле
    },
  },
} */
export default {
  name: 'signIn',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login(event) {
      event.preventDefault();

      // логика авторизации
      // пост запрос, на сервер джанги по api - получения токена
      this.axios
        // отправляю post запрос на сервер джанго, передаю туда values полей username и password
        // данные из полей на сервере фронтенда
        .post('http://localhost:8000/api/auth/token', { username: this.username, password: this.password })
        // получаю ответ отправленный с сервера джанги, получаю токен и пердаю в метод setLogined
        .then((response) => { this.setLogined(response.data.token); })
        // отработка ошибок?
        .catch((err) => { console.error(err); });
    },
    setLogined(token) {
      // отправляю токен в консоль
      console.log(token);
      // сохраняю токен - его можно будет использовать уже в пермишен api
      localStorage.setItem('token', token);
    },
  },
};
</script>

<!-- Cтиль для текущего компонента -->
<style scoped>

</style>
