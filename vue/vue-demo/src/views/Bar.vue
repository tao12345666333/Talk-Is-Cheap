<template>
  <div>
    <vue-datepicker :time.sync="date" :option="timeoption"></vue-datepicker>
    {{ date }}
  </div>
</template>

<script>
import vueDatepicker from 'vue-datepicker';

export default {
  components: {
    vueDatepicker,
  },
  data() {
    return {
      timeoption: {
        type: 'min',
        week: ['一', '二', '三', '四', '五', '六', '日'],
        month: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
        format: 'YYYY-MM-DD HH:mm',
        placeholder: '请选择上线时间'
      },
      date: '',
    }
  },
}
</script>

<style>
</style>
