<template>
  <div id="app">
    <header id="header" class="header">
      <div class="logo">
        <img src="./assets/logo.png" alt="">
      </div>
    </header>
    <div class="mark">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menu: [{
        urlName: 'mark',
        name: 'Markdown',
      }],
    };
  },
};
</script>

<style>
html {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

#app {
  color: #2c3e50;
  margin-top: -100px;
  max-width: 600px;
  font-family: Source Sans Pro, Helvetica, sans-serif;
  text-align: center;
}

#app a {
  color: #42b983;
  text-decoration: none;
}

.logo {
  float: left;
  margin-right: 10px;
}

.logo img {
  width: 40px;
  height: 40px;
}

code {
  color: #e96900;
  padding: 3px 5px;
  border-radius: 2px;
  white-space: nowrap;
}

</style>
