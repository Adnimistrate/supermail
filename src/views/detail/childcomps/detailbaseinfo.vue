<template>
  <div  class="base-info">
    <div class="info-title">{{goodsinfo[2]}}</div>
    <div class="info-price">
      <span class="n-price">{{goodsinfo[3]}}</span>
      <span class="o-price">{{goodsinfo[4]}}</span>
      <span class="discount">{{goodsinfo[5]}}</span>
    </div>
    <div class="info-other">
      <span>{{goodsinfo[7]}}{{goodsinfo[6]}}</span>
      <span>{{goodsinfo[9]}}{{goodsinfo[8]}}</span>
      <span>{{goodsinfo[10]}}</span>
    </div>
    <div class="infoervice">
        <span >
        <img src="../../../assets/img/common/ture.png">
        {{goodsinfo[11]}}
      </span>
    <span >
        <img src="../../../assets/img/common/ture.png">
        {{goodsinfo[12]}}
    </span>
    </div>
  </div>
</template>

<script>
	export default {
		name: "detailbaseinfo",
    props: {
		  goodsinfo: {
		    type: Array,
        default(){
          return []
        }

      }
    }
	}
</script>

<style >
  .base-info {
    margin-top: 15px;
    padding: 0 8px;
    color: #999;
    border-bottom: 5px solid #f2f5f8;
  }

  .info-title {
    color: #222
  }

  .info-price {
    margin-top: 10px;
  }

  .info-price .n-price {
    font-size: 28px;
    padding-left: 1%;
    color: red;
  }

  .info-price .o-price {
    font-size: 13px;
    margin-left: 2%;
    text-decoration: line-through;
  }

  .info-price .discount {
    font-size: 12px;
    padding: 2px 5px 2px 5px;
    color: #fff;
    background-color: red;
    border-radius: 8px;
    margin-left: 10px;

    /* 让元素上浮一些: 使用相对定位即可*/
    position: relative;
    top: -8px;
  }

  .info-other {
    margin-top: 15px;
    line-height: 30px;
    display: flex;
    font-size: 13px;
    border-bottom: 1px solid rgba(22, 20, 20, 0.1);
    justify-content: space-between;
  }

  .infoervice {
    display: flex;
    justify-content: space-between; /* 平均分配flex空间 */
    height: 50px;
    line-height: 50px;
    color: red;
    font-size: 5px;
  }

  .infoervice img {
    width: 14px;
    height: 14px;
    top: 2px;
  }

</style>
