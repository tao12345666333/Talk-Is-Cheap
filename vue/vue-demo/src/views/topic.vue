<template>
  <div class="container">
    <div>
      <button @click="next">Next page</button>
    </div>
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
      page: 1,
    };
  },
  methods: {
    next() {
      this.page += 1;
      api.topic.list(this.page, resp => {
        this.topics = resp.data.data;
      });
    },
  },
  route: {
    data(transition) {
      api.topic.list(this.page, resp => {
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
