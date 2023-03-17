<template>
  <div class="sign_component">
    <h3>components/auth/SignIn.vue компонент</h3>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
// разрешаю экспорт текущего компонента auth/components/auth/SignIn.vue
export default {
  name: 'signIn',
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- Написал стиль для текущего компонента -->
<style scoped>
.sign_component {
  background-color: #ffc4c4;
}
</style>
