<template>
  <div class="detailproduct">
    <div v-for='item in productdata'>
      <img :src="item[2]" alt="">
    </div>
  </div>
</template>
<script>
  export default {
name:'detailproduct',
props:{
  productdata:{
    type:Array,
    default(){
      return[]
    }
  }
}
  }
</script>
<style>
  .detailproduct{
    padding: 20px;
  }
  .detailproduct img{
    width: 100%;
    height: 100%;
    border-radius: 20px;
  }
</style>