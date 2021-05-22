<template>
  <div class="checkbar" :class='{check:ischeck}'>
    <img src="../../../assets/img/cart/tick.svg" alt="">
  </div>
</template>
<script>
  export default {
name:'checkbar',
props:{
  ischeck:{
    type:Boolean,
    default:false
  }
}
  }
</script>
<style>
  .checkbar{
    border-radius: 50%;
    border: 2px solid #aaa;
  }
  .check{
    border-color: red;
    background-color: red;
  }
</style>