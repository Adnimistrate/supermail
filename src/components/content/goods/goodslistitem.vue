<template>
  <div class="goodslistitem" @click='itemclick' >
    <img :src="goodsitem[2]" alt="" @load='imgfinish'>
    <div class="goodsinfo">
      <p>{{goodsitem[3]}}</p>
    
      <div class="pandc">
      <span class="price">{{goodsitem[4]}}</span>
      <span class="loveimg"><img src="../../../assets/img/common/collect.svg" alt=""></span>
      <span class="collect">{{goodsitem[5]}}</span>
    </div>
    
  </div>
  </div>
</template>
<script>
  export default {
name:'goodslistitem',
props:{
  goodsitem:{
    type:Array,
    default(){
      return []
    }
  }
},
  methods: {
    itemclick(){
      this.$router.push('/detail/'+this.goodsitem[6])  //+this.goodsitem[6]，router.push直接跳转到某页面不需要引入，只要router的index里面写了就行
    },
    imgfinish(){
      //因为home和detail都用了这个组不知道谁发的事件
      if(this.$route.path.indexOf('/home')!==-1){
        this.$bus.$emit('homeimgfinish')
      }
      else if(this.$route.path.indexOf('/detail')!==-1){
        this.$bus.$emit('detailimgfinish')
      }
    }
  },


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
  bottom: 0px; /* 跟图片留空隙 */
  left: 0;
  right: 0;
  overflow: hidden; /* 超出的东西隐藏 */
  text-align: center;

  }
  .goodsinfo p{
    margin-top: 3px;
    overflow: hidden; /* 超出的文字隐藏 */
    text-overflow: ellipsis;   /* 超出的文字用...显示 */
    white-space: nowrap;  /* 文字不分行一行显示 */
    margin-bottom: 3px;

  }

.pandc{
  align-items: center;
}
.loveimg img{
    width: 14px;
    height: 14px; 
    top: -1px;
    
}
.price{
  color: red;
  margin-right: 10px;
  font-weight: lighter;
  font-family: fantasy;
  font-size: medium;
}
.collect{
  color: black;
  font-family: sans-serif;
}
</style>