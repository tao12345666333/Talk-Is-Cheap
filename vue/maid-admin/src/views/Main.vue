<template>
  <div class="main">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {};
  },
  created() {
    console.log('mian');
  },
};
</script>

<style>
</style>
