<template>
<div class="toast" v-show='show'>  <!-- 动态绑定show由detail传递决定 -->
  <div>  
    {{message}}
  </div>

</div>
</template>
<script>
  export default {
name:'toast',
// props:{
//   //方法1
//   message:{
//     type:String,
//     default:''
//   },
//   show:{
//     type:Boolean,
//     default:false
//   }
// },
data() {
  return {
    message:'',
    show:false
  }
},
methods: {
  isshow(message='默认值',time=2000){
    this.show=true
    this.message=message
    setTimeout(()=>{
    this.show=false
    this.message=''
    },time)
  }
},
  }
</script>
<style>
  .toast{
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%); /* 居中显示 */
  padding: 8px 10px;
  color: #ffffff;
  background-color: rgba(0,0,0,.35);
  z-index: 999;
}
</style>