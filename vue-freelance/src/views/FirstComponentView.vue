<template>
  <div class="first_view">
    <h1>Розовый-компонент, голубой-представление, синий-main.js(общий компонент)</h1>
    <hr><br><br><br>
    <!-- Использую компонент first/FirstComponent.vue (смотри скрипт этого файла) -->
    <FirstComponent msg="пробное (см props компонента)" />
    <!-- вызываю компонент 4 раза -->
    <FirstComponent />
    <FirstComponent />
    <FirstComponent />
    <FirstComponent />
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>Моё первое представление FirstComponentView - src/views/FirstComponentView.vue</h1>
    <h2>{{ viewDataMsg }}</h2>
  </div>
</template>

<script>
// @ is an alias to /src
// импортирую компоненты components/first/FirstComponent.vue
import FirstComponent from '@/components/first/FirstComponent.vue';

export default {
  // имя шаблона
  name: 'FirstComponentView',
  // добавляю компоненты
  components: {
    FirstComponent,
  },
  // создаю свой конструктор, сообщения для вызова {{ viewDataMsg }}
  data() {
    return {
      viewDataMsg: 'Это {{ viewDataMsg }} в FirstComponentView.vue',
    };
  },
};
</script>

<!-- Написал стиль для текущего компонента -->
<style scoped>
.first_view {
  background-color: #8ef9ff;
}
</style>
