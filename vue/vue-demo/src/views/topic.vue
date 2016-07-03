<template>
  <div class="container">
    <topic-item v-for="topic in topics" :topic="topic">
    </topic-item>
  </div>
</template>

<script>
import api from '../api';
export default {
  data() {
    return {
      topics: [],
    };
  },
  route: {
    data(transition) {
      api.topic.list(resp => {
        transition.next({
          topics: resp.data.data,
        });
      });
    },
  },
};
</script>

<style>
</style>
