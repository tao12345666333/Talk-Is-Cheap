<template>
  <div class="main">
    <ul class="nav-tabs">
      <li v-for="tab in tabs">
        <a href="javascript:;" @click="changeCurrentTab(tab.ename)">{{ tab.name }}</a>
      </li>
    </ul>
    <div class="tab-content">
      {{ currentTab }}
    </div>
  </div>
</template>

<script>
// import api from '../api';
export default {
  data() {
    return {
      tabs: [],
      currentTab: '',
    };
  },
  route: {
    data(transition) {
      // api.tabset.list(resp => {
      //   transition.next({
      //     tabs: JSON.parse(resp.data).data,
      //   });
      // });
      transition.next({
        tabs: [
          {
            name: 'tab1',
            ename: 'tab1',
          },
          {
            name: 'tab2',
            ename: 'tab2',
          },
          {
            name: 'tab3',
            ename: 'tab3',
          },
        ],
      });
    },
  },
  methods: {
    changeCurrentTab(tab) {
      this.$set('currentTab', tab);

      // api.tabset.list(resp => {
      //   this.$set('datas', resp.data.data);
      //   this.$set('tabs', [{ name: 'test' }]);
      // });
    },
  },
};
</script>

<style lang="less">

.main {
  margin: 5px 8px 10px 12px;
}

.nav-tabs {
  border-bottom: 1px solid #ddd;
}
</style>
