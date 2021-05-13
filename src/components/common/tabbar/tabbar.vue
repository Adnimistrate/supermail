<template>
  <div id="tabbar">
<slot></slot>
  </div>
</template>
<script>
  import tabbaritem from './tabbaritem.vue'
export default {
  name: 'tabbar',
  components: {
    tabbaritem
  },
}
</script>
<style>
  #tabbar{
  display: flex;
  background-color: rgb(143, 188, 167);

  position: fixed;
  left: 0ch;
  right: 0;
  bottom: 0;
  box-shadow: 0px -3px 1px black;
}
</style>
