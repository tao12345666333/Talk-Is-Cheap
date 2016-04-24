<template>
  <div id="header" class="header">
    <a class="logo">
      <img src="./assets/logo.png" alt="">
      <span>Vue-Markdown-Editor</span>
    </a>
    <ul class="nav">
      <li>
        <a href="https://github.com/tao12345666333/Talk-Is-Cheap">Github</a>
      </li>
    </ul>
  </div>
  <div class="mark">
    <router-view></router-view>
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
  font-size: 15px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #34495e;
  margin: 0;
}

a {
  text-decoration: none;
  color: #34495e;
}

.logo {
  display: inline-block;
  font-size: 1.5em;
  line-height: 40px;
  color: #2c3e50;
  font-family: 'Dosis', 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif;
  font-weight: 500;
}

.logo img {
  vertical-align: middle;
  margin-right: 6px;
  width: 40px;
  height: 40px;
}

#header {
  background-color: #fff;
  box-shadow: 0 0 4px rgba(0,0,0,0.25);
  padding: 25px 60px;
  position: relative;
  z-index: 2;
}

.nav {
    list-style-type: none;
    margin: 0;
    padding: 0;
    position: absolute;
    right: 60px;
    top: 25px;
    height: 40px;
    line-height: 40px;
}

</style>
