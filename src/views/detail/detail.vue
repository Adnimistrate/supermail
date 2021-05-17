<template>
  <div class="detail">
    <detailnavbar></detailnavbar>
    <detaiswiper :detaildata='detaildata'></detaiswiper>
    <detailbaseinfo :goodsinfo='goodsinfo'></detailbaseinfo>
    <detailshop :shopdata='shopdata'></detailshop>

    <backtop @click.native='backclick'></backtop>
  </div>
</template>
<script>
  
  import detailnavbar from './childcomps/detailnavbar.vue'
  import detaiswiper from './childcomps/detailswiper.vue'
  import detailbaseinfo from './childcomps/detailbaseinfo.vue'
  import detailshop from './childcomps/detailshop.vue'

  import backtop from '../../components/common/backtop/backtop.vue'

  import {getdetailsdata,getgoodsinfo,getshopdata} from '../../network/detail.js'
  export default {
name:'detail',
components:{
  detailnavbar,
  detaiswiper,
  detailbaseinfo,
  detailshop,

  backtop
},
data() {
  return {
    iid:null,
    detaildata:[],
    goodsinfo:[],
    shopdata:[],
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
    console.log(result.data[0]);
  this.shopdata=result.data[0]
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
}
  
</script>
<style>
</style>