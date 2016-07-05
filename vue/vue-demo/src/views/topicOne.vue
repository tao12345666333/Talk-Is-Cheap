<template>
  <div>
    <h1>{{ topic.title }}/h1>

    <div>
      <div>{{ topic.content }}</div>
    </div>
  </div>
</template>

<script>
import api from '../api';

export default {
  data() {
    return {
      topic: {},
    };
  },
  route: {
    data(transition) {
      const id = transition.to.params.topicId;
      api.topic.detail(id, resp => {
        transition.next({
          topic: resp.data.data
        });
      });
    },
  },
};

</script>

<style>
</style>
