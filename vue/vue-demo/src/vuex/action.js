const initNote = {
  id: +new Date(),
  title: 'OneNote',
  content: 'OneNote Content',
};

const initData = {
  notes: [initNote],
  activeNote: initNote,
};

export const initStore = ({ dispatch }) => {
  dispatch('initStore', initData);
};
