<template>
  <div class="navbar">
    <!-- //搞几个插超，导航栏每个页面都不一样，可能第一个页面左边是返回中间标题右边搜索 -->
    <!-- 用div包起来比较好 -->
   <div class="left"> <slot name='left'></slot></div>
   <div class="center"> <slot name='center'></slot></div>
   <div class="right"> <slot name='right'></slot></div>

  </div>
</template>
<script>
  export default {
name:'navbar',
  }
</script>
<style>
  .navbar{
    /* //flex布局为盒子模型，就是变成一个盒子，固定每个东西的宽度高度 */
    /* //就是划分左右中占的大小 */
    display: flex;
    line-height: 44px;
    height: 44px;
    text-align: center;
    box-shadow: 0 1px 1px rgba(100 100 100 0.1); 
  }，
  .left,.right,.left{
    width: 60px;

  }
  .center{
    flex: 1;
  }
</style>