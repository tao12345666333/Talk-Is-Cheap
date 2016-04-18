<template>
  <div class="preview">
    <h1 v-if="true">{{ msg }}</h1>
    <template v-if="true">
      <div v-for="(i, m) in nmsg">
        the {{ i }} is {{ m }}
      </div>
    </template>
    <template v-else>
      <h1>else {{msg}}</h1>
    </template>

    <div>
      <span v-for="n in 10">{{ n }}</span>
    </div>
  </div>

  <div class="preview">
    <div>
      <button v-on:click="on_btn">Click</button>
    </div>
  </div>

  <div class="preview">
    <div>
      <div>Input: {{ t }}</div>
      <input type="text" v-model="t" placeholder="input here">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'Hello World!',
      nmsg: ['a', 'b', 'c'],
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
