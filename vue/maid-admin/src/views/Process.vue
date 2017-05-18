<template>
  <div class="process">
    show xhr process {{ process }}
  </div>
</template>

<script>
export default {
  name: 'Process',
  data() {
    return {
      process: 0,
    };
  },
  methods: {
    updateProcess(evt) {
      console.log(evt);
      console.log('updateProcess');
      if (evt.lengthComputable) {
        this.process = evt.loaded / evt.total;
      } else {
        this.process = 'can not compute';
      }
    },
    transferComplete(evt) {
      console.log(evt);
      console.log('complete');
    },
  },
  created() {
    console.log('c');
    const req = new XMLHttpRequest();

    req.addEventListener('progress', this.updateProcess, false);
    req.addEventListener('load', this.transferComplete, false);

    req.open('get', 'http://moelove.info');
    req.send();
  },
};
</script>

<style>
.process {
  position: absolute;
  top: 30px;
  left: 20px;
}
</style>
