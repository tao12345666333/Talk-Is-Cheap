<template>
  <div>
    <div id="notes-list">
      <div class="header">
        <div class="form-group">
          <input name="title" type="text" v-model="currentNote.title">
          <textarea name="content" cols="30" rows="10" v-model="currentNote.content">
          </textarea>
        </div>
      </div>
      <div class="content">
        <div v-for="note in Notes">
          <div>
            <h2>{{ note.title }}</h2>
          </div>
          <div>
            <p>{{ note.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from '../vuex/store';
import { initStore } from '../vuex/action';
import { Notes, activeNote } from '../vuex/getter';

export default {
  store,
  vuex: {
    actions: {
      initStore,
    },
    getters: {
      Notes,
      activeNote,
    },
  },
  computed: {
    currentNote: activeNote,
  },
  ready() {
    this.initStore();
  },
};
</script>

<style lang="less" scoped>
</style>
