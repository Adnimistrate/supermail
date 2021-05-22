<template>
  <div class="detailshopbar">
    <div class="baritem barleft">
      <div>
        <i class="icon service"></i>
        <span class="text">客服</span>
      </div>
      <div>
        <i class="icon shop"></i>
        <span class="text">店铺</span>
      </div>
      <div>
        <i class="icon select"></i>
        <span class="text">收藏</span>
      </div>
    </div>
    <div class="baritem barright">
      <div class="cart" @click="addtocart">加入购物车</div>
      <div class="buy">购买</div>
    </div>
  </div>
</template>
<script>
  export default {
name:'detailshopbar',
methods: {
  addtocart(){
    console.log('+++++');
    this.$emit('addtocart')
  }
},
  }
</script>
<style>
.detailshopbar{
  height: 58px;
  position: fixed;
  background-color: #fff;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  text-align: center;

}
.baritem {
  flex: 1;
  display: flex;
}

.baritem>div {
  flex: 1;
}

.barleft .text {
  font-size: 13px;
}

.barleft .icon {
  display: block;
  width: 22px;
  height: 22px;
  margin: 10px auto 3px;
  background: url("~assets/img/detail/detail_bottom.png") 0 0/100%;
}

.barleft .service {
  background-position:0 -54px;
}

.barleft .shop {
  background-position:0 -98px;
}

.barright {
  font-size: 15px;
  color: #fff;
  line-height: 58px;
}

.barright .cart {
  background-color: #ffe817;
  color: #333;
}

.barright .buy {
  background-color: #f69;
}
</style>