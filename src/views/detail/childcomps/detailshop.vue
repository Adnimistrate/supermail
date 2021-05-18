<template>
  <div class="detailshop">
    <div class="shopname">
   <img :src="shopdata[2]" alt="">
   <span class="shoptitle">{{shopdata[3]}}</span> <!-- //记得用span包起文字好设置样式 -->
    </div>

    <div class="shop-middle"> 
      <div class="shop-middle-left">
        <div class="sells">
          <div class="sells-num">  <!-- 数字和文字都用一个div包着就会上下排列 -->
            {{shopdata[5] | sellCountFilter}}
          </div>
          <div class="sells-name">
            总销量
          </div>
        </div>
        <div class="allgoods">
          <div class="goods-num">
            {{shopdata[6]}}
          </div>
          <div class="goods-name">
            全部宝贝
          </div>

        </div>

      </div>
      <div class="shop-middle-right">
        <div class="marktop">
        <span>描述相符：</span>
        <span  :class='{active:markrank(shopdata[7])}'>{{shopdata[7]}}{{rank}}</span>
      </div>
      <div class="markmiddle">
        <span>价格合理：</span>
        <span  :class='{active:markrank(shopdata[8])}'>{{shopdata[8]}}{{rank}}</span>
      </div>
      <div class="markbottom">
        <span>质量满意：</span>
        <span  :class='{active:markrank(shopdata[9])}' >{{shopdata[9]}}{{rank}}</span>
      </div>


      </div>
      </div>
      <div class="shop-bottom">
        <div class="enter-shop">进店逛逛</div>
      </div>
    </div>
    
  </div>
</template>
<script>
  export default {
name:'detailshop',
props:{
  shopdata:{
    type:Array,
    default(){
      return []
    }
  }
},
data() {
  return {
    rank:'高'
  }
},
filters:{
  sellCountFilter(value){
    if(value<10000)
    {
      return value
    }
    else
    return ((value/10000).toFixed(1)+'万')

  }
},
methods: {
  markrank(index){
    if (index>3.5)
    {
      this.rank='高'
      return true
    }
    else if(index>2.5&&index<3.5)
   { this.rank='中'
    return false
  }
    else
    {
      this.rank='低'
      return false
    }
  }
},
  }
</script>
<style>
  .detailshop{
    padding: 25px 8px;
    border-bottom: 5px solid #f2f5f8;
  }
  .shopname{
    line-height: 45px;
    display: flex;
    align-items: center;     /* 让元素垂直中心对齐 */
  }
.shopname img{
  width: 46px;
  height: 45px;
  border-radius: 50%;  /* 边框圆角 */
  border: 1px solid rgba(0,0,0,.1);
}
.shoptitle{
  margin-left: 13px;     /* margin排外距离 */
  vertical-align: center; /* 文字纵向居中，text-align横向居中 */
  color: black;
}
.shop-middle {
    margin-top: 15px;
    display: flex;
    align-items: center;
  }
  .shop-middle-left{
    flex: 1;
    display: flex;
    justify-content: space-evenly;
    color: #333;
    text-align: center;  
  }
  .sells-num, .goods-num{
    font-size: 18px;
  }
  .sells-name, .goods-name{
    margin-top: 10px;
    font-size: 12px;
  }
.shop-middle-right{
  width: 120px;
  margin-left: 30px;
  margin-right: 20px
}
.marktop ,.markmiddle, .markbottom{
  margin-top: 2px;
}
.active{
  color: red;
}
.shop-bottom{
  text-align: center;
  margin-top: 10px;
}
.enter-shop{
  display: inline-block; /* 占据一行居中显示 */
  font-size: 14px;
  background-color: #f2f5f8;
  width: 150px;
  height: 30px;
  text-align: center;
  line-height: 30px;
  border-radius: 30px;


}

</style>