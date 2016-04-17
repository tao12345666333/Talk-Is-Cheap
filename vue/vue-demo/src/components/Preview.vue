<template>
  <div class="preview">
    <h1 v-if="true">{{ msg }}</h1>
    <template v-if="false">
      <h1>if {{ nmsg }}</h1>
    </template>
    <template v-else>
      <h1>else {{msg}}</h1>
    </template>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'Hello World!',
      nmsg: 'vim',
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #669933;
}
</style>
