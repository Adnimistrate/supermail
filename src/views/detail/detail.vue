<template>
  <div class="detail">
    <detailnavbar class="detailnavbars" @titleclick="titleclick"></detailnavbar
    ><!-- 监听子组件发出的点击和index -->
   <detaiswiper :detaildata="detaildata"></detaiswiper>
    <detailbaseinfo :goodsinfo="goodsinfo"></detailbaseinfo>
    <detailshop :shopdata="shopdata"></detailshop>
    <detailproductinfo :productinfodata="productinfodata"></detailproductinfo>
    <detailproduct ref="product" :productdata="productdata"></detailproduct>
    <!-- ref是可以拿el或者组件或者div的任何数据-->
    <detailmark ref="mark" :markdatafirst="markdatafirst"></detailmark>
    <goodslist
      @detailimgfinish="detailimgfinish"
      ref="recommend"
      :currentgoods="goodsrecommand"
    ></goodslist>
    <detailshopbar @addtocart='addtocart'></detailshopbar>
    <backtop @click.native="backclick"></backtop>
    <!-- <toast :message='message' :show='show'></toast> -->
  </div>
</template>
<script>
import detailnavbar from "./childcomps/detailnavbar.vue";
import detaiswiper from "./childcomps/detailswiper.vue";
import detailbaseinfo from "./childcomps/detailbaseinfo.vue";
import detailshop from "./childcomps/detailshop.vue";
import detailproductinfo from "./childcomps/detailproductinfo.vue";
import detailproduct from "./childcomps/detailproduct.vue";
import detailmark from "./childcomps/detailmark.vue";
import detailshopbar from "./childcomps/detailshopbar.vue";
import goodslist from "../../components/content/goods/goodslist.vue";

import backtop from "../../components/common/backtop/backtop.vue";
import toast from "../../components/common/toast/toast.vue";

import {
  getdetailsdata,
  getgoodsinfo,
  getshopdata,
  getproductdata,
  getproductinfodata,
  getproductmarkdata,
  getgoodsrecommanddata
} from "../../network/detail.js";
export default {
  name: "detail",
  components: {
    detailnavbar,
    detaiswiper,
    detailbaseinfo,
    detailshop,
    detailproductinfo,
    detailproduct,
    detailmark,
    goodslist,
    detailshopbar,

    backtop,
    // toast,
  },
  data() {
    return {
      iid: null,
      detaildata: [],
      goodsinfo: [],
      shopdata: [],
      productdata: [],
      productinfodata: [],
      markdatafirst: [],
      markdataall: [],
      goodsrecommand: [],
      movetoY: [], //参数商品评论推荐对应的地方
      // message:null,  //传递给toast的信息
      // show:false,   //弹窗是否显示
    };  
  },
  created() {
    this.iid = this.$route.params.iid; //用route.params拿到链接的iid
    getdetailsdata(this.iid).then(result => {
      this.detaildata = result.data;
    }),
      getgoodsinfo(this.iid).then(result => {
        this.goodsinfo = result.data[0];
      });
    getshopdata(this.iid).then(result => {
      this.shopdata = result.data[0];
    });
    getproductdata(this.iid).then(result => {
      this.productdata = result.data;
    });
    getproductinfodata(this.iid).then(result => {
      this.productinfodata = result.data[0];
    });
    getproductmarkdata(this.iid).then(result => {
      this.markdataall = result.data;
      this.markdatafirst = result.data[0];
    });
    getgoodsrecommanddata(this.iid).then(result => {
      this.goodsrecommand = result.data;
    });
  },
  methods: {
    backclick() {
      const that = this;
      let timer = setInterval(() => {
        let ispeed = Math.floor(-that.scrollTop / 5);
        document.documentElement.scrollTop = document.body.scrollTop =
          that.scrollTop + ispeed;
        if (that.scrollTop === 0) {
          clearInterval(timer);
        }
      }, 16);
    },

    //监听子组件图片加载完成，就可以获取推荐评论等等的滚轮位置  ----失败！！！！
    detailimgfinish() {
      // this.movetoY = [];
      // this.movetoY.push(0);
      // this.movetoY.push(this.$refs.product.$el.offsetTop);
      // this.movetoY.push(this.$refs.mark.$el.offsetTop);
      // this.movetoY.push(this.$refs.recommend.$el.offsetTop);
    },

    //监听子组件发出的点击和index
    titleclick(index) {
      this.movetoY = [];
      this.movetoY.push(0);
      this.movetoY.push(this.$refs.product.$el.offsetTop);
      this.movetoY.push(this.$refs.mark.$el.offsetTop);
      this.movetoY.push(this.$refs.recommend.$el.offsetTop);
      window.scrollTo(0, this.movetoY[index], 1000); //移动到对应的位置（0，-y）延时100ms
    },

    //监听子组件加入购物车
    addtocart(){
     // 1.获取购物车需要展示信息
     const products={}
     products.iid=this.iid
     products.img=this.productdata[0][2]
     products.title=this.goodsinfo[2]
     products.price=this.goodsinfo[3]
     products.shop=this.shopdata[3]

     // 2.将商品添加到购物车（vuex，组件不同用￥bus比较难）
     //通过store发送数据（在main.js注册就行了，直接使用）
    this.$store.dispatch('addtocart',products).then(res=>{

    //3.显示添加购物车成功（弹窗显示（封装组件到处用））
       //promise中resolve传过来的信息用.then可以打印信息
       //1.麻烦方法 普通封装
      //  this.show=true
      //  this.message='aaaaaaa'
       
      //  setTimeout(()=>{
      //   this.show=false
      //  this.message=''
      //  },1500)
      


    //1.高级方法 main.js注册$toast,index.js封装函数调用toast.vue
    //最后用$toast调用toast.isshow函数
    this.$toast.isshow(res,2000)

  
   }) 
    },

    //为了计算距离顶部的高度，当高度大于60显示回顶部图标，小于60则隐藏
    scrollToTop() {
      const that = this;
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      that.scrollTop = scrollTop;
      if (that.scrollTop > 30) {
        that.btnFlag = true;
      } else {
        that.btnFlag = false;
      }
    }
  },
  mounted() {
    window.addEventListener("scroll", this.scrollToTop);
  },
  destroyed() {
    window.removeEventListener("scroll", this.scrollToTop);
  },
  //打开新页面默认从最上的时候开始
  updated() {
    window.scroll(0, 0);
  }
};
</script>
<style>
.detailnavbars {
  position: sticky; /* 粘性定位 */
  /* 当我滑到一定位置的时候系统自动会改成fiex */
  top: 2px; /*就是划着划着这个导航栏会固定住，不会被划上去 */
  z-index: 9;
  background-color: rgb(248, 248, 255);
}
</style>
