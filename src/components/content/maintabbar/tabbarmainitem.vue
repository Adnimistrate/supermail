<template>
  <tabbar>

    <tabbaritem path='/Home' >
      <img slot='itemicon' src="../../../assets/img/tabbar/home.svg" alt="">
      <img slot='itemiconactive' src="../../../assets/img/tabbar/home_active.svg" alt="">
      <div slot='itemtext'>首页</div>
    </tabbaritem>
    <tabbaritem path='/Category'>
      <img slot='itemicon' src="../../../assets/img/tabbar/category.svg" alt="">
      <img slot='itemiconactive' src="../../../assets/img/tabbar/category_active.svg" alt="">
      <div slot='itemtext'>分类</div>
    </tabbaritem>
    <tabbaritem path='/Cart'>
      <img slot='itemicon' src="../../../assets/img/tabbar/cart.svg" alt="">
      <img slot='itemiconactive' src="../../../assets/img/tabbar/cart_active.svg" alt="">
      <div slot='itemtext'>购物车</div>
    </tabbaritem>
    <tabbaritem path='/Profile'>
      <img slot='itemicon' src="../../../assets/img/tabbar/profile.svg" alt="">
      <img slot='itemiconactive' src="../../../assets/img/tabbar/profile_active.svg" alt="">
      <div slot='itemtext'>我的</div>
    </tabbaritem>
  </tabbar>
</template>
<script>
    import tabbar from '../../common/tabbar/tabbar.vue'
    import tabbaritem from '../../common/tabbar/tabbaritem.vue'
  export default {
name:'tabbarmainitem',
components:{
  tabbar,
  tabbaritem
}
  }
</script>
<style>
</style>