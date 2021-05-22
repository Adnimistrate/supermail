<template>
  <div class="cartlist">
    <cartlistitem v-for='(item,index) in cartlist' :key='index' :cartlist='item'></cartlistitem>
    
  </div>
</template>
<script>
  import cartlistitem from './cartlistitem.vue'
  export default {
name:'cartlist',
components:{
  cartlistitem,
},
data() {
  return {
    cartlist:this.$store.state.shopcart
  }
},
  }
</script>
<style>
  .cartlist{
    margin-top: 30px;
    width: 100%;
    height: 80%;
    padding: 25px 8px;
    border-bottom: 5px solid #f2f5f8;

  }
</style>