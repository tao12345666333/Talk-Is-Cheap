<template>
  <div id="mark">
    <textarea :value="input" debounce="300" @input="update"></textarea>
    <div v-html="input"></div>
  </div>
</template>

<script>
export default {
  name: 'editor',
  data() {
    return {
      input: 'editor',
    };
  },
  methods: {
    update: (e) => {
      console.log(this);
      this.input = e.target.value;
    },
  },
};
</script>

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
