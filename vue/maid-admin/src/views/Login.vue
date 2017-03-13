<template>
  <section class="index" style="background: black;">
    <div class="desc">
      <div class="all_center" style="top: 30%; left: 40%;">
        <h2>这是一个使用 Vue 2.0 的应用</h2>
        <p>Maid System</p>
        <p> ©2017 </p>
      </div>
    </div>
    <div class="login">
      <h2>请点击按钮登录</h2>
      <a class="submit" >登录</a>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Main',
};
</script>

<style scoped>
.index {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.desc {
  position: fixed;
  top: 50%;
  left: 25%;
  width: 800px;
  height: 400px;
  margin-top: -200px;
  margin-left: -250px;
  color: #fff;
  animation: fadeInLeftBig 0.7s ease 0s 1 both;
  -webkit-animation: fadeInLeftBig 0.7s ease 0s 1 both;
  -moz-animation: fadeInLeftBig 0.7s ease 0s 1 both;
  -ms-animation: fadeInLeftBig 0.7s ease 0s 1 both;
}

.desc h2 {
  font-size: 22px;
  text-align: center;
  line-height: 88px;
}

.desc p {
  font-size: 16px;
  line-height: 66px;
  text-align: center;
}

.login {
  width: 400px;
  height: 260px;
  border: 1px solid rgba(255, 255, 255, 0.9);
  border-radius: 6px;
  position: fixed;
  left: 75%;
  top: 50%;
  margin-left: -200px;
  margin-top: -200px;
  padding: 20px;
  box-sizing: border-box;
  animation: fadeInRightBig 0.7s ease 0s 1 both;
  -webkit-animation: fadeInRightBig 0.7s ease 0s 1 both;
  -moz-animation: fadeInRightBig 0.7s ease 0s 1 both;
  -ms-animation: fadeInRightBig 0.7s ease 0s 1 both;
  background-color: rgba(255, 255, 255, 0.2);
}

.login h2 {
  color: #fff;
  font-size: 24px;
  font-weight: normal;
  line-height: 38px;
}

.login form {
  width: 100%;
  display: block;
  margin-top: 20px;
}

.login form>label {
  width: 100%;
  display: block;
  border: 1px solid #fff;
  border-radius: 4px;
  height: 38px;
  margin-top: 25px;
  position: relative;
}

.login form label i {
  display: block;
  width: 26px;
  height: 26px;
  position: absolute;
  color: #fff;
  font-size: 26px;
  font-weight: 300;
  margin-top: 4px;
  line-height: 26px;
  padding: 0;
  left: 10px;
}

.login form>label input {
  display: block;
  width: 100%;
  height: 100%;
  border: none;
  padding: 0 10px;
  margin: 0;
  font-size: 14px;
  box-sizing: border-box;
  text-indent: 36px;
  background: rgba(0, 0, 0, 0);
  color: #fff;
}

.login form label input::-moz-placeholder {
  color: rgba(255, 255, 255, 0.8);
}

.login form label input::-webkit-input-placeholder {
  color: rgba(255, 255, 255, 0.8);
}

.login form label input:-ms-input-placeholder {
  color: rgba(255, 255, 255, 0.8);
}

.login form label input:-webkit-autofill {
  -webkit-text-fill-color: #fff !important;
  transition: background-color 5000s ease-in-out 0s;
}

.login form label:first-child {
  margin-top: 0px;
}

.remember {
  color: #fff;
  font-size: 12px;
  line-height: 32px;
  -webkit-text-size-adjust: none;
  -webkit-user-select: none;
  margin-top: 15px;
}

.remember>label {
  cursor: pointer;
}

.remember>label input {
  display: inline-block;
  vertical-align: middle;
  margin-right: 5px;
}

.errors {}

.errors p {
  font-size: 12px;
  color: #f50;
  line-height: 20px;
}

.submit {
  display: block;
  font-size: 18px;
  width: 80%;
  height: 38px;
  border: 1px solid rgba(255, 255, 255, 0.7);
  padding: 0;
  margin: 56px auto 0;
  line-height: 38px;
  color: #fff;
  background: rgba(0, 0, 0, 0);
  cursor: pointer;
  text-align: center;
  border-radius: 4px;
  clear: both;
  transition: all ease 0.2s;
  -webkit-transition: all ease 0.2s;
  -moz-transition: all ease 0.2s;
  -ms-transition: all ease 0.2s;
}

.submit:hover {
  background: rgba(0, 0, 0, 0.1);
}

</style>
