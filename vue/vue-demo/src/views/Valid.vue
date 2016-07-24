<template>
  <div class="valid">
    <validator name="validation">
      <form novalidate>
        <div class="form-group">
          <label>Name: </label>
          <input class="form-control" type="text" v-model="info.name" v-validate:name="{ required: true, minlength: 4 }">
          <div class="valid-msg" v-if="$validation.name.required">Required your name</div>
        </div>
        <div class="form-group">
          <label>Content: </label>
          <input class="form-control" type="text" v-model="info.content" v-validate:content="{ required: true, minlength: 10 }">
          <div class="valid-msg" v-if="$validation.content.minlength">minlength is 10</div>
          <div class="valid-msg" v-if="$validation.content.required">Content is required</div>
        </div>
        <div class="form-group">
          <label>Num: </label>
          <input class="form-control" type="text" v-model="info.num">
        </div>
        <div class="form-group">
          <label>Email: </label>
          <input class="form-control" type="email" v-model="info.email">
        </div>
        <button v-if="$validation.valid" @click="" type="submit" class="btn btn-default">Submit</button>
      </form>
    </validator>
  </div>
</template>

<script>
export default {
  data() {
    return {
      info: {
        name: 'This is info name',
        content: 'This is test info content',
        num: 1,
        email: 'test@example.com',
      },
    };
  },
};
</script>

<style lang="less">
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: 700;
}

.btn {
  display: inline-block;
  padding: 6px 12px;
  margin-bottom: 0;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 4px;
}

.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}

.valid {
  margin-top: 18px;
  width: 60%;
}

.form-group {
  margin-bottom: 16px;
}

.form-control {
  display: block;
  width: 100%;
  height: 34px;
  padding: 6px 12px;
  font-size: 14px;
  line-height: 1.42857143;
  color: #555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
  -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
}

.valid-msg {
  margin-top: 16px; 
  background-color: #FFEEE6;
  border: 1px solid #fdc;
  width: 18%;
}
</style>
