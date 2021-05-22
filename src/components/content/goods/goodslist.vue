<template>

  <div class="goods" > 
    <goodslistitem v-for='item in currentgoods' :goodsitem='item' ></goodslistitem><!-- //拿到home数据后在进一步传给gooditem.vue -->
    <div class="end">END</div> 
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
},
  }
</script>
<style>
  .goods{
    display: flex; /* 整体盒子模型，不然没有4宫格 */
    flex-wrap: wrap; /* 不包裹，可以设置goodlistitem的宽度决定一行多少个 */
    justify-content: space-around; /* 图片均等分 */
    margin-bottom: 70px ;
    border-bottom: 5px solid #f2f5f8;
  }
  .end{
  display: inline-block; /* 占据一行居中显示 */
  font-size: 14px;
  background-color: #f2f5f8;
  width: 150px;
  height: 30px;
  text-align: center;
  line-height: 30px;
  border-radius: 30px;
  margin-bottom: 5px ;
  border-bottom: 5px solid #f2f5f8;
    
  }

</style>