import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  notes: [],
  activeNote: {},
  show: '',
};

const mutations = {
  initStore(state, data) {
    state.notes = data.notes;
    state.show = data.show;
    state.activeNote = data.activeNote;
  },

  newNote(state) {
    const nnote = {
      id: +new Date(),
      title: '',
      content: '',
    };

    state.notes.push(nnote);
    state.activeNote = nnote;
  },

  editNote(state, note) {
    state.activeNote = note;

    for(let i =0; i < state.notes.length; i++) {
      if(state.notes[i].id === note.id) {
        state.notes[i] = note;
        break;
      }
    }
  },

  setActiveNote(state, note) {
    state.activeNote = notes;
  },
};

export default new Vuex.Store({
// share
  state,
  mutations,
});
