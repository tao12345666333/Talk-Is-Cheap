<template>
  <div id="app">
    <router-view keep-alive>
    </router-view>
    <home></home>
  </div>
</template>

<script>
import Hello from './components/Hello';
import Home from './components/Home';

export default {
  name: 'app',
  components: {
    Hello,
    Home,
  },
  template: '<h1>Test</h1>',
};
</script>

<style>
</style>
