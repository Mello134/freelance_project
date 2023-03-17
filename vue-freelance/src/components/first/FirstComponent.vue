<template>
  <div class="first_component">
    <h3>Мой первый компоент - components/firts/FirstComponent.vue</h3>
    <!-- Если в представлении, при выхове компонента будет msg='какойто_текст, он появится' -->
    <h1>{{ msg }}</h1>
    <h1>{{ msg }}</h1>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
// разрешаю экспорт текущего компонента src/components/first/FirstComponent.vue
export default {
  // это имя компонента чтобы вызавть <FirstComponent />
  name: 'FirstComponent',
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- Написал стиль для текущего компонента FirstComponent.vue -->
<style scoped>
.first_component {
  background-color: #ffc4c4;
}
</style>
