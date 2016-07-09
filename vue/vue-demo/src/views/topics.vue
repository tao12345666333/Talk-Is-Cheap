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
    };
  },
  methods: {
    next() {
      api.topic.list(this.$route.params.pageNum, resp => {
        this.topics = resp.data.data;
      });
    },
  },
  route: {
    data(transition) {
      api.topic.list(this.$route.params.pageNum, resp => {
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
