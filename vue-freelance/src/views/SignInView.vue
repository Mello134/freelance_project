<template>
  <div class="signin_view">
    <h1>Розовый-компонент, голубой-представление, синий-main.js(общий компонент)</h1>
    <hr><br><br><br>
    <!-- использую компонент auth/SignIn.vue (смотри скрипт этого файла) -->
    <SignIn msg="пробное (см props компонента"/>
    <!-- вызываю компонент 4 раза -->
    <SignIn />
    <SignIn />
    <SignIn />
    <SignIn />
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>SignIn - Представление - src/views/SignInView.vue</h1>
    <h2>{{ viewDataMsg }}</h2>
  </div>
</template>

<script>
// @ is an alias to /src
// импортирую компоненты components/auth/SignIn.vue
import SignIn from '@/components/auth/SignIn.vue';

export default {
  name: 'SignInView',
  components: {
    SignIn,
  },
  // создаю свой конструктор, сообщения для вызова {{ viewDataMsg }}
  data() {
    return {
      viewDataMsg: 'Это {{ viewDataMsg }} в SignInVue.vue',
    };
  },
};
</script>

<!-- Написал стиль для текущего компонента -->
<style scoped>
.signin_view {
  background-color: #8ef9ff;
}
</style>
