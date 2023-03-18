<!-- eslint-disable vuejs-accessibility/label-has-for -->
<template>
  <div class="w-50 border rounded p-3 mx-auto">
    <b-form @submit="register">
      <div class="form-group p-2">
        <label for="username">Логин:</label>
        <b-input v-model="username" type="text" id="username" placeholder="Логин.."></b-input>
      </div>
      <div class="form-group p-2">
        <label for="phone">Номер телефона:</label>
        <b-input v-model="phone" type="text" id="phone" placeholder="+7 (921) 123 45 67"></b-input>
      </div>
      <div class="form-group p-2">
        <label for="customerOrExecutor" class="pe-3">Вы заказчик или исполнитель?</label>
        <b-select
          v-model="customerOrExecutor"
          :options="customerOrExecutorOptions"
          type="customerOrExecutor"
          id="customerOrExecutor"
        ></b-select>
      </div>
      <div class="form-group p-2">
        <label for="password">Пароль:</label>
        <b-input v-model="password" type="password" id="password" placeholder="Пароль.."></b-input>
      </div>
      <div class="form-group p-2">
        <label for="repeatPassword">Повторите пароль:</label>
        <b-input
          v-model="repeatPassword"
          type="password"
          id="repeatPassword"
          placeholder="Повторите пароль.."
        ></b-input>
      </div>
      <b-button variant="primary" type="submit" class="m-2">Регистрация</b-button>
      <p class="mt-3">
        Уже есть аккаунт?
        <router-link to="/auth/signin">Вход</router-link>
      </p>
    </b-form>
  </div>
</template>

<script>
/* разрешаю экспортировать текущий компонент {
  имя компонента: 'SignUp',
  данные компонента() - пользуюсь ими в тегах html {
    вернуть (возвращает сразу) {
      username: изначально пусто,
      пароль: изначально пусто,
      повторить пароль: изначально пусто,
      телефон: изначально пусто,
      исполнитель или заказчик: изначально пусто,
      чойсы: [выберете../заказчик/исполнитель],
    };
  },
  методы: {
    регистрация(событие) {
      обработчик события, регистрации
      // логика ругистрации - подробно внутри
    }
  }
} */
export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      password: '',
      repeatPassword: '',
      customerOrExecutor: '',
      customerOrExecutorOptions: [
        {
          text: 'Выберите...',
          value: '',
          disabled: true,
          selected: true,
        },
        { text: 'Заказчик', value: 'customer' },
        { text: 'Исполнитель', value: 'executor' },
      ],
    };
  },
  methods: {
    register(event) {
      event.preventDefault();

      // логика регистрации
      // отправляю api пост запрос на сервер django
      // пока работает только имя и пароль (чойсы, телефон не катит)
      this.axios.post('http://localhost:8000/api/auth/users/', {
        username: this.username, password: this.password,
        // после успешной регистрации, параметры респонса в консоль и перекидывает на маршрут войти
      }).then((response) => { console.log(response); this.$router.push('/auth/signin'); })
        .catch((err) => { console.error(err); });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
