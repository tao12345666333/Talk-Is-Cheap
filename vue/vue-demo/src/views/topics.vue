<template>
  <div class="container">
    <div>
      <button @click="next"  v-link="{ name: 'topics', params: { pageNum: page } }">Next page</button>
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
      page: parseInt(this.$route.params.pageNum, 0),
    };
  },
  methods: {
    next() {
      this.page += 1;
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
