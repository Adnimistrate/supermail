<template>
  <div class="cartlistitem">
    <div class="select">
    <checkbar :ischeck='cartlist.checked'
    @click.native='checkclick'></checkbar>  <!-- //传递后台的checked信息,点击改变后台的为false -->
  </div>
    <div class="productimg">
      <img :src="cartlist.img" alt="商品图片">
    </div>
    <div class="productinfo" >
      <div class="producttitle">{{cartlist.title}}</div>
      <div class="productshop">店铺名称: {{cartlist.shop}}</div>
      <div class="productinfobottom">
        <span class="productinfoprice">{{cartlist.price}}</span>
        <span class="productinfocount">x{{cartlist.count}}</span>
      </div>
    </div>

  </div>
</template>
<script>
  import checkbar from '../../../components/content/checkbar/checkbar.vue'
  export default {
name:'cartlistitem',
props:{
  cartlist:{
    type:Object,
    default(){
      return {}
    }
  }
},
components:{
  checkbar,
},
methods: {
  checkclick(){
    this.cartlist.checked=!this.cartlist.checked  //点击取反后台数据
  }
},
  }
</script>
<style>
.select{
  display: flex;
  align-items: center; 
  width: 14%;
  justify-content: center;
}

  .cartlistitem {
  width: 100%;
  display: flex;
  font-size: 0;
  padding: 5px;
  border-bottom: 1px solid #ccc;
}
.productimg{
  padding: 5px;
}

.productimg img{
  height: 80px;
  width: 100px;
  border-radius: 5px;
}
.productinfo{
  padding: 5px;
  position: relative;
  overflow: hidden;
  font-size: 17px;
  color: black;
  font-family: cursive;
}
.producttitle,.productshop{
  overflow: hidden;  /* 多余文本隐藏 */
  white-space: nowrap;/* 文本不换行 */
  text-overflow: ellipsis; /* 多余文本用... */
}
.productinfo，.productshop{
  font-size: 14px;
  color: #666;
  margin-top: 15px;
}
.productinfobottom{
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
}

.productinfoprice, .productinfobottom{
  color: red;
  font-size: 17px;
  font-family: fantasy;
}

</style>