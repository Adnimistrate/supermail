<template>
  <div class="goodslistitem">
    <img :src="goods1item[2]" alt="">
    <div class="goodsinfo">
      <p>{{goods1item[3]}}</p>
      <span class="price">{{goods1item[4]}}</span>
      <span class="collect">{{goods1item[5]}}</span>
    </div>
  </div>
</template>
<script>
  export default {
name:'goodslistitem',
props:{
  goods1item:{
    type:Array,
    default(){
      return []
    }
  }

}
  }
  
</script>
<style>
  .goodslistitem{
    padding-bottom: 40px;
    position: relative;  /* 下面有绝对就有相对的 */
    width: 48%;  /* 跟goodslist里面的home配合，一行显示2个*/
  }
  .goodslistitem img{
    width: 100%;
    border-radius: 5px;  /* 图片圆角 */
  }
  .goodsinfo{ /* 包文字和价格之类的diy */
  font-size: 12px;
  position: absolute; /* 位置绝对的 */
  bottom: 5px; /* 跟图片留空隙 */
  left: 0;
  right: 0;
  overflow: hidden; /* 超出的东西隐藏 */
  text-align: center;

  }
  .goodsinfo p{
    overflow: hidden; /* 超出的文字隐藏 */
    text-overflow: ellipsis;   /* 超出的文字用...显示 */
    white-space: nowrap;  /* 文字不分行一行显示 */
    margin-bottom: 3px;

  }
  .goodsinfo .price{
    color: red;
    margin-right: 20px;
  }

  .goodsinfo .collect{
    position: relative; /* 下面有绝对就有相对的 */
  }
  .goodsinfo .collect::before{  /* 在collect之前 */
    content: '';
    position: absolute;
    left: -15px;
    top: -1px;
    width: 14px;
    height: 14px; 
    background: url('../../../assets/img/common/collect.svg');
  }

</style>