<template>
  <div>
    <ul v-for="tab in tabs">
      <li>
        <a href="javascript:;" @click="changeCurrentTab(tab.ename)">{{ tab.name }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
import api from '../api';
export default {
  data() {
    return {
      tabs: [],
      currentTab: '',
    };
  },
  route: {
    data(transition) {
      api.tabset.list(resp => {
        transition.next({
          tabs: JSON.parse(resp.data).data,
        });
      });
    },
  },
  methods: {
    changeCurrentTab(tab) {
      this.$set('currentTab', tab);

      api.tabset.list(resp => {
        this.$set('datas', resp.data.data);
        this.$set('tabs', [{ name: 'test' }]);
      });
    },
  },
};
</script>

<style>
</style>
