<template>
  <div id="home">
    <!-- //首页就需要个标题就行了替换center的插超 -->
    <navbar class="homenav"><div slot='center'>购物街</div></navbar>
     <!-- //记住要用v-bind --> <!-- //用v-bind传到子组件props里面 ,这里的homeswiper就是子组件的拿到后送到props-->
    <homeswiper :banners='banners'></homeswiper>
  </div>
</template>
<script>
  import navbar from '../../components/common/navbar/navbar.vue'
  import homeswiper from './childcomps/homeswiper.vue'
  import {gethomedata} from '../../network/home.js'
  export default {
name:'Home',
components:{
  navbar,
  homeswiper
},

data() {
  return {
    banners:[],
    recommends:[]
  }
},
//生命周期函数，创建完成发送网络请求
created() {
  //调用函数在home.js里面，.then成功后打印结果
  gethomedata().then(result=>{
    //保存到全局变量
     this.banners=result.data
     console.log(result.data);
    // this.recommends=result.data.recommend.list
  })
},
  }
</script>
<style>
  .homenav{
    background-color: pink;
    color: white;
  }
</style>