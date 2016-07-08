<template>
  <div>
    <a v-link="{name: 'detail', params: {topic_id: topic.id}}">
      <h3>{{ topic.title }}</h3>
    </a>
    <h4>{{ topic.id }}</h4>
    <div>
      {{ topic.content }}
    </div>
  </div>
</template>

<script>

import api from '../api';
export default {
  props: {
    topic: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  route: {
    data(transition) {
      api.topic.detail(this.$route.params.topic_id, resp => {
        transition.next({
          topic: resp.data.data,
        });
      });
    },
  },
};
</script>

<style>
</style>
