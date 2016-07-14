<template>
  <div>
    <ul v-for="tab in tabs">
        <li>{{ tab.name }}</li>
    </ul>
  </div>
</template>

<script>
import api from '../api';
export default {
  data() {
    return {
      tabs: [],
    };
  },
  route: {
    data(transition) {
      api.tabset.list(resp => {
        transition.next({
          tabs: JSON.parse(resp.data).data,
        });
      });
    },
  },
};
</script>

<style>
</style>
