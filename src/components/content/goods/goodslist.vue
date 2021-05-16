<template>

  <div class="goods"> 
    <goodslistitem v-for='item in currentgoods' :goods1item='item'></goodslistitem><!-- //拿到home数据后在进一步传给gooditem.vue -->

  </div>
</template>
<script>
  import goodslistitem from './goodslistitem'
  export default {
name:'goodslist',
components:{
  goodslistitem
},
props:{
  currentgoods:{
    type:Array,
    default(){
      return []
    }
  }
}
  }
</script>
<style>
  .goods{
    display: flex; /* 整体盒子模型，不然没有4宫格 */
    flex-wrap: wrap; /* 不包裹，可以设置goodlistitem的宽度决定一行多少个 */
    justify-content: space-around; /* 图片均等分 */
  }
</style>