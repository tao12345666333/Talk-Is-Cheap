<template>
  <div class="container">
    <ul>
      <li v-for="topic in topics">
        {{ topic.title }}
      </li>
    </ul>
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
    getTopics() {
    },
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
