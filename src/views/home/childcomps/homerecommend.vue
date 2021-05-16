<template>
  <div class="homerecommend">
    <div v-for='item in recommends' class="homerecommenditem"> 
<a :href="item[1]"></a>
<img :src="item[2]" alt="">
<div>{{item[3]}}</div>
    </div>

  </div>
</template>
<script>
  export default {
name:'homerecommend',
props:{
  recommends:{
    typeof:Array,
    default:[]
  }
}
  }
</script>
<style>
  .homerecommend{
    display: flex;  /*盒子模型*/
    text-align: center;  /*文字居中*/
    font-size: 12px;  /*文字大小*/
    padding: 15px 0 20px 0;  /*设置上右下左空隙，更好看*/
    border-bottom: 8px solid #eee; /*设置下边框大小和颜色，一条灰线分隔*/

  }
  .homerecommenditem{
    flex: 1; /*均等分 */
  }

  .homerecommenditem img{
    width: 65px;  /* 设置图片大小 */
    height: 65px;
    margin-bottom: 10px; /* 设置图片文字距离 */
  }
</style>