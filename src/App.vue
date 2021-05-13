<template>
  <div id="app">
     <!-- routerview决定渲染位置，相当于占个坑，渲染的页面会覆盖这个 -->
<router-view></router-view>
<tabbarmainitem></tabbarmainitem>
  </div>
</template>
<script>
  import tabbarmainitem from './components/content/maintabbar/tabbarmainitem.vue'
  export default {
name:'App',
components:{
  tabbarmainitem

}
  }
</script>
<style>
  @import './assets/css/base.css'
</style>