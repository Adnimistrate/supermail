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
   /* 用fixe可以固定位置，但是要设置leftrightbottom等
   用relative是相对的多少内容就放在内容下面一点点 */
  position: fixed;
  left: 0ch;
  right: 0;
  bottom: 0;
  box-shadow: 0px -3px 1px black;
  z-index: 10;
}
</style>
