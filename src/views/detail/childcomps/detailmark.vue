<template>
  <div class="detailmark">
    <div class="marktitle">
      <span>用户评价</span>
      <span><a href="">更多</a></span>
    </div>
    <div class="user">
      <span><img :src="markdatafirst[2]" alt=""></span>
      <span class="usertitle">{{markdatafirst[3]}}</span>

    </div>
    <div class="mark">
      <span ><p>{{markdatafirst[4]}}</p></span>
    </div>
    <div class="userthing">
      <span>{{markdatafirst[5]}}</span>
      <span>颜色：{{markdatafirst[6]}}</span>
      <span>尺码：{{markdatafirst[7]}}</span>
    </div>
    <div class="userimg">
      <span><img :src="markdatafirst[8]" alt=""></span>
    </div>
  </div>
</template>
<script>
  export default {
name:'detailmark',
props:{
  markdatafirst:{
    type:Array,
    default(){
      return []
    }
  }
},
  }
</script>
<style>
  .detailmar{
    padding: 20px;
  }
  .marktitle{
    padding: 20px;
    display: flex;
    justify-content: space-between;
    border-bottom: 5px solid #f2f5f8;
  }
  .user{
    padding: 10px;
    border-bottom: 5px solid #f2f5f8;
    display: flex;
    align-items: center;     /* 让元素垂直中心对齐 */
  }
  .user img{
    width: 44px;
    height: 44px;
    border-radius: 50%;  /* 边框圆角 */
  }
  .usertitle{
  margin-left: 13px;     /* margin排外距离 */
  font-weight: bolder;
  }
  .mark{
    font-weight: lighter;
    line-height: 20px;
    text-indent:2em;
    overflow: hidden; /* 超出的东西隐藏 */
    text-overflow: ellipsis;   /* 超出的文字用...显示 */
  }
  .userthing{
    padding: 10px;
    border-bottom: 5px solid #f2f5f8;
    display: flex;
    justify-content: space-between;
    align-items: center;     /* 让元素垂直中心对齐 */
  }
  .userimg{
    padding: 20px;
    margin-bottom: 60px ;
    border-bottom: 5px solid #f2f5f8;

  }
  .userimg img{
    width: 100px;
    height: 100px;
    
  }
</style>