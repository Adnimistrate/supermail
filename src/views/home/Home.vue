<template>
  <div id="home">
    <!-- //首页就需要个标题就行了替换center的插超 -->
    <navbar class="homenav"><div slot='center'>购物街</div></navbar>
     <!-- //记住要用v-bind --> <!-- //用v-bind传到子组件props里面 ,这里的homeswiper就是子组件的拿到后送到props-->
    <homeswiper :banners='banners'></homeswiper>
    <homerecommend :recommends='recommends'></homerecommend>
    <featureview></featureview>
    <tabcontrol class='tabcontrol' :titles="['流行','新款','精选']"
    @tabclick='tabclick'></tabcontrol>  <!-- 因为子组件传了数据点了哪个，这里是监听 -->
    <goodslist :currentgoods='currentgoods'></goodslist>

    <tabbarmainitem></tabbarmainitem>
    <backtop @click.native='backclick'></backtop> <!-- 我们监听一个组件的原生事件时候要加.native 比如div的点击 -->
    
  </div>
</template>
<script>
  //导入home下面子组件
  import homeswiper from './childcomps/homeswiper.vue'
  import homerecommend from './childcomps/homerecommend.vue'
  import featureview from './childcomps/featureview.vue'
  
  //导入公共组件
  import navbar from '../../components/common/navbar/navbar.vue'
  import tabcontrol from '../../components/content/tabcontrol/tabcontrol.vue'
  import goodslist from '../../components/content/goods/goodslist.vue'
  import backtop from '../../components/common/backtop/backtop.vue'
  import tabbarmainitem from "../../components/content/maintabbar/tabbarmainitem.vue";
  
  //导入网络请求函数
  import {getbannersdata,getrecommendsdata} from '../../network/home.js'
  import {getgoods1data,getgoods2data,getgoods3data} from '../../network/home.js'

  export default {
name:'Home',
components:{
  homeswiper,
  homerecommend,
  featureview,
  navbar,
  tabcontrol,
  goodslist,
  backtop,
  tabbarmainitem

},

data() {
  return {
    banners:[],
    recommends:[],  
    goods1:[],
    goods2:[],
    goods3:[],
    currentgoods:[], //goods当前数据
  }
},
methods: {
  //事件监听子组件方法
  //goods点击
  tabclick(index){
    switch(index){
      case 0:
        this.currentgoods=this.goods1
        break;
      case 1:
        this.currentgoods=this.goods2
        break;
      case 2:
        this.currentgoods=this.goods3
        break;
    }
  },
  //回到顶部点击
  // 点击图片回到顶部方法，加计时器是为了过渡顺滑
  backclick () {
      const that = this
      let timer = setInterval(() => {
        let ispeed = Math.floor(-that.scrollTop / 5)
        document.documentElement.scrollTop = document.body.scrollTop = that.scrollTop + ispeed
        if (that.scrollTop === 0) {
          clearInterval(timer)
        }
      }, 16)
  },
 
  //为了计算距离顶部的高度，当高度大于60显示回顶部图标，小于60则隐藏
  scrollToTop () {
    const that = this
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
    that.scrollTop = scrollTop
    if (that.scrollTop > 30) {
      that.btnFlag = true
    } else {
      that.btnFlag = false
    }
  }
},
//生命周期函数，创建完成发送网络请求
created() {
  //调用函数在home.js里面，.then成功后打印结果

  getbannersdata().then(result=>{

    //保存到全局变量
     this.banners=result.data
  })
  getrecommendsdata().then(result=>{

    //保存到全局变量
     this.recommends=result.data
  })
  getgoods1data().then(result=>{

    //保存到全局变量
     this.goods1=result.data
     this.currentgoods=result.data  //默认拿第一个数据
  })
  getgoods2data().then(result=>{
 
    //保存到全局变量
     this.goods2=result.data
  })
  getgoods3data().then(result=>{
    //保存到全局变量
     this.goods3=result.data
  })
},
// vue的两个生命钩子，这里不多解释。
// window对象，所有浏览器都支持window对象。它表示浏览器窗口，监听滚动事件
mounted () {
  window.addEventListener('scroll', this.scrollToTop)
},
destroyed () {
  window.removeEventListener('scroll', this.scrollToTop)
},
  }
</script>
<style>
  #home{
     /* 下面两个东西重叠设置了导航栏优先会挡住其他，
     要把他撑起，离上面一定距离 */
    padding-top: 44px; 
  }
  .homenav{
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


  .tabcontrol{
    position: sticky;  /* 粘性定位 */
    /* 当我滑到一定位置的时候系统自动会改成fiex */
    top: 44px; /* 就是划着划着这个导航栏会固定住，不会被划上去 */
    z-index: 9; /* 防止被别人盖住 */
  }
</style>