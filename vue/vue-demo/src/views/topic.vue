<template>
  <div class="container">
   <ul>
     <li v-for="topic in topics">
       {{ topic.name }}
     </li>
   </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      topics: [
        { name: 's' },
        { name: 't' },
      ],
    };
  },
  methods: {
    getTopics() {
    },
  },
};
</script>

<style>
</style>
