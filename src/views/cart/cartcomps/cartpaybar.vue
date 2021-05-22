<template>
  <div class="cartpaybar">
    <div class="checkall">
      <checkbar class="checkbutton" 
      :ischeck='ischeckall' 
      @click.native='checkallclick'></checkbar>  <!-- 用.native监组件的点击 -->
      <span>全选</span>
    </div>
    <div class="price">
      合计：{{totalprice}}
    </div>
    <div class="paymoney" @click='paymoney'>
      结算:{{checknum}}
    </div>
  </div>
</template>
<script>
    import checkbar from '../../../components/content/checkbar/checkbar.vue'
  export default {
name:'cartpaybar',
components:{
  checkbar,
},
computed:{
  totalprice(){
    //用filter过滤没选择的,item就是之前的$store.state.shopcart
    //返回那些选择了的数据
    //reduce（）方法会接收一个函数作为累加器，对上面选择了的数据进行运算
    //每执行一次保存到prevalue,最后每次乘完后都要加上之前的数据
    return '￥'+this.$store.state.shopcart.filter(item=>{
      return item.checked
    }).reduce((prevalue,item)=>{
      return prevalue+item.price*item.count
    },0).toFixed(2)
  },
  checknum(){
    //先过滤数据
    //任何返回过滤数据的长度
    return this.$store.state.shopcart.filter(item=>{
      return item.checked
    }).length
  },
  ischeckall(){
    //法1效率低会遍历全部，如果有没选择的就会有长度，取反就为false
    // return !this.$store.state.shopcart.filter(item=>!item.checked).length

    //法二只要找到没选择的就停止,find找到没选择然后的返回内容，取反就是false
    if(this.$store.state.shopcart.length==0) return false
    else
    return !this.$store.state.shopcart.find(item=>!item.checked)


    //法三普通遍历
    // for(let item of this.$store.state.shopcart){
    //   if(!item.checked){
    //     return false
    //   }
      
    // }
    // return true
  },

},
methods: {
  checkallclick(){
    //foreach循环用于列举出集合中所有的元素
    if(this.ischeckall){
      //如果true就遍历把所有的checked都改为false
      this.$store.state.shopcart.forEach(item=>item.checked=false)
    }
    else{
      this.$store.state.shopcart.forEach(item=>item.checked=true)
    }
  },
  paymoney(){
    if(!this.ischeckall){
      this.$toast.isshow('请选择商品！',2000)
    }
  }
},


  }
</script>
<style>
  .cartpaybar{
  background-color: #eee;
     /* 用fixe可以固定位置，但是要设置leftrightbottom等
   用relative是相对的多少内容就放在内容下面一点点 */
  position: fixed;
  left: 0;
  right: 0;
  bottom: 8.5%;
  display: flex;
  height: 50px;
  line-height: 50px;
  border-radius: 10%;
  }
  .checkall{
  display: flex;
  align-items: center;
  font-size: 13px;
  margin-left: 10px;
  width: 60px;
  }
  .checkbutton{
   width: 20px;
   height: 20px;
   line-height: 20px;
   margin-right: 10px;
  }
  .price{
  color: red;
  padding-left: 50px;
  flex: 1;
  font-size: 13px;
  }
  .paymoney{
  width: 90px;
  color: white;
  text-align: center;
  background-color: #ff8198;
  font-size: 14px;
  border-radius: 10%;
  margin-right: 4%;
  }
</style>