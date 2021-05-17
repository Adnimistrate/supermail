<template>
  <div id="app">
    <!-- routerview决定渲染位置，相当于占个坑，渲染的页面会覆盖这个 -->

      <keep-alive exclude='detail'>
        <!-- 默认会缓存 把detail排除在外，离开页面就销毁，返回时在点击会重新获取iid然后请求数据 -->
      <router-view></router-view> 
      </keep-alive>
    <tabbarmainitem></tabbarmainitem>
  </div>
</template>
<script>
import tabbarmainitem from "./components/content/maintabbar/tabbarmainitem.vue";
export default {
  name: "App",
  components: {
    tabbarmainitem
  }
};
</script>
<style>
@import "./assets/css/base.css";
</style>
