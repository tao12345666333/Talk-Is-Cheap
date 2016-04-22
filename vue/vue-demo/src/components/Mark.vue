<template>
  <div id="mark">
    <textarea v-model="input" debounce="300"></textarea>
    <div v-html="input | imarked"></div>
  </div>
</template>

<script>
const marked = require('marked');
export default {
  data() {
    return {
      input: '# Hello World!',
    };
  },
  filters: {
    imarked: marked,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
