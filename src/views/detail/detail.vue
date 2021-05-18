<template>
  <div class="detail">
    <detailnavbar class="detailnavbars"></detailnavbar>
    <detaiswiper :detaildata='detaildata'></detaiswiper>
    <detailbaseinfo :goodsinfo='goodsinfo'></detailbaseinfo>
    <detailshop :shopdata='shopdata'></detailshop>
    <detailproductinfo :productinfodata='productinfodata'></detailproductinfo>
    <detailproduct :productdata='productdata'></detailproduct>
    <detailmark :markdatafirst='markdatafirst'></detailmark>

    <backtop @click.native='backclick'></backtop>

  </div>
</template>
<script>
  
  import detailnavbar from './childcomps/detailnavbar.vue'
  import detaiswiper from './childcomps/detailswiper.vue'
  import detailbaseinfo from './childcomps/detailbaseinfo.vue'
  import detailshop from './childcomps/detailshop.vue'
  import detailproductinfo from './childcomps/detailproductinfo.vue'
  import detailproduct from './childcomps/detailproduct.vue'
  import detailmark from './childcomps/detailmark.vue'

  import backtop from '../../components/common/backtop/backtop.vue'

  import {getdetailsdata,getgoodsinfo,getshopdata,getproductdata,getproductinfodata,getproductmarkdata} from '../../network/detail.js'
  export default {
name:'detail',
components:{
  detailnavbar,
  detaiswiper,
  detailbaseinfo,
  detailshop,
  detailproductinfo,
  detailproduct,
  detailmark,

  backtop
},
data() {
  return {
    iid:null,
    detaildata:[],
    goodsinfo:[],
    shopdata:[],
    productdata:[],
    productinfodata:[],
    markdatafirst:[],
    markdataall:[]
  }
},
created() {
  this.iid=this.$route.params.iid //用route.params拿到链接的iid
  getdetailsdata(this.iid).then(result=>{
  this.detaildata=result.data
  }),
  getgoodsinfo(this.iid).then(result=>{
  this.goodsinfo=result.data[0]
  })
  getshopdata(this.iid).then(result=>{
  this.shopdata=result.data[0]
  })
  getproductdata(this.iid).then(result=>{
  this.productdata=result.data
  })
  getproductinfodata(this.iid).then(result=>{
  this.productinfodata=result.data[0]
  })
  getproductmarkdata(this.iid).then(result=>{
  console.log(result.data);
  this.markdataall=result.data
  this.markdatafirst=result.data[0]
  })
},
methods: {

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
mounted () {
  window.addEventListener('scroll', this.scrollToTop)
},
destroyed () {
  window.removeEventListener('scroll', this.scrollToTop)
},
//打开新页面默认从最上的时候开始
updated() {
    window.scroll(0, 0);
  },
 }
  
</script>
<style>
    .detailnavbars{
    position: sticky;  /* 粘性定位 */
    /* 当我滑到一定位置的时候系统自动会改成fiex */
    top: 2px; /*就是划着划着这个导航栏会固定住，不会被划上去 */
    z-index: 9;
    background-color: rgb(248, 248, 255);
   } 
</style>