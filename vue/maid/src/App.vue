<template>
  <div id="app">
    <router-view keep-alive>
    </router-view>
    <mmain></mmain>
  </div>
</template>

<script>
import Hello from './components/Hello';
import Mmain from './components/Main';

export default {
  name: 'app',
  components: {
    Hello,
    Mmain,
  },
  template: '<h1>Test</h1>',
};
</script>

<style>
</style>
