<template>
  <div class="productinfo">
    <div class="brandname">
      <span>
        品牌名称:{{productinfodata[2]}}
      </span>
    </div>
    <div class="goodsinfo">
      产品参数：
    </div>
    <div class="firtinfo">
      <span>品牌:{{productinfodata[2]}}</span>
      <span>适应年龄:{{productinfodata[3]}}</span>
      <span>尺码:{{productinfodata[4]}}</span>
    </div>
    <div class="twoinfo">
      <span>图案:{{productinfodata[5]}}</span>
      <span>流行风格:{{productinfodata[6]}}</span>
      <span>通勤:{{productinfodata[7]}}</span>
    </div>
    <div class="threeinfo">
      <span>领型:{{productinfodata[8]}}</span>
      <span>流行元素:{{productinfodata[9]}}</span>
      <span>颜色:{{productinfodata[10]}}</span>
    </div>
    <div class="fourinfo">
      <span>袖型:{{productinfodata[11]}}</span>
      <span>产品货号:{{productinfodata[12]}}</span>
      <span>图案:{{productinfodata[13]}}</span>
    </div>
    <div class="fiveinfo">
      <span>袖长:{{productinfodata[15]}}</span>
      <span>年份季节:{{productinfodata[14]}}</span>
      <span>衣长:{{productinfodata[16]}}</span>
    </div>
    <div class="sixinfo">
      <span>服装版型:{{productinfodata[17]}}</span>
      <span>销售渠道:{{productinfodata[18]}}</span>
      <span>材质成分:{{productinfodata[19]}}</span>
    </div>
  </div>
</template>
<script>
  export default {
name:'detailproductinfo',
props:{
  productinfodata:{
    type:Array,
    default(){
      return []
    }
  }
}
  }
</script>
<style>
    .productinfo{
    padding: 20px;
  }
  .brandname{
    padding: 10px;
    font-weight: lighter;
  }
  .goodsinfo{
    padding: 10px;
    font-weight: lighter;
  }
  .firtinfo ,.twoinfo,.threeinfo,.fourinfo,.fiveinfo,.sixinfo{
    margin: 12px ; /*设置下边框大小和颜色，一条灰线分隔*/
    font-size: 10px;
    display: flex;
    justify-content: space-between;
    white-space: nowrap;  /* 文字不分行一行显示 */
    overflow: hidden; /* 超出的文字隐藏 */
    text-overflow: ellipsis;   /* 超出的文字用...显示 */
    text-align: center;
    align-items: center;
    font-weight: bolder;
    
  
  }
</style>