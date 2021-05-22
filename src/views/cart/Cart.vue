<template>
  <div class="Cart">
  <navbar class="cartnav"><div slot='center'>购物车({{cartlength}})</div></navbar>
  <cartlist></cartlist>
  <cartpaybar class="paybar"></cartpaybar>
  <tabbarmainitem></tabbarmainitem>

  </div>
</template>
<script>
  import navbar from '../../components/common/navbar/navbar.vue'
  import cartlist from './cartcomps/cartlist.vue'
  import cartpaybar from './cartcomps/cartpaybar.vue'
  import tabbarmainitem from "../../components/content/maintabbar/tabbarmainitem.vue";
  export default {
name:'Cart',
components:{
  navbar,
  cartlist,
  cartpaybar,


  tabbarmainitem
},
computed:{
  cartlength(){
  return this.$store.state.shopcart.length
}
  },
}
</script>
<style>
    .cartnav{
    background-color: pink;
    color: white;
    position: fixed;  /* 固定顶部导航栏，不然一拉进度条不见了 */
    left: 0;
    right: 0;
    top: 0;
    /*两个用了position=..就象
    桌子上的纸张一样，位于上面的肯定会挡住下面的,设置谁优先显示在上面越大越先*/
    z-index:9 ; 
  }
</style>