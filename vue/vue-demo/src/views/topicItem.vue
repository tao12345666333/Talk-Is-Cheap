<template>
  <div>
    <h3>{{ topic.title }}</h3>
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
      default: {},
    },
  },
  route: {
    data(transition) {
      api.topic.detail((id, resp) => {
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
