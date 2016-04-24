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

#mark, body, html {
  margin: 0;
  height: 100%;
  font-family: Arial,sans-serif;
  color: #333;
}

textarea {
  border: none;
  border-right: 1px solid #ccc;
  resize: none;
  outline: none;
  background-color: #f6f6f6;
  font-size: 15px;
  font-family: courier,monospace;
  padding: 20px;
  min-height: 900px;
}

#mark div, textarea {
  display: inline-block;
  width: 49%;
  height: 100%;
  vertical-align: top;
  box-sizing: border-box;
  padding: 20px 20px;
}

</style>
