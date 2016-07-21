<template>
  <div>
  </div>
</template>

<script>
import store from '../vuex/store';
import { initStore } from '../vuex/action';

export default {
  store,
  vuex: {
    actions: {
      initStore,
    },
  },
};
</script>

<style>
</style>
