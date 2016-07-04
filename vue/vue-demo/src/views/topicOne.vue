<template>
  <div>
    <h1>{{ topic.title }}/h1>

    <div>
      <div>{{ topic.content }}</div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      topic: Object,
    };
  },
}; 

</script>

<style>
</style>
