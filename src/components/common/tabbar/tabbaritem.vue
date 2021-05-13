<template>
  <div class="tabbaritem" @click='itmclick()'>
    <div v-if='!isactive'><slot  name='itemicon'></slot></div>
    <div v-else><slot  name='itemiconactive'></slot></div>
    <div :style='activestyle'><slot  name='itemtext'></slot></div>

    </div>
</template>
<script>
  export default {
name:'tabbaritem',
props:{
  path:String,
  activecolor:{
    type:String,
    default:'deeppink'
  }
},
methods: {
  itmclick(){
    this.$router.replace(this.path)
  }
},
computed:{
  isactive(){
    //判断当前路由路径和点击标签的路径是否一样
    //一样的赋值true
    return this.$route.path.indexOf(this.path)
  },

  activestyle(){
    //绑定样式，判断有没有点击点击后赋值color
    return this.isactive ?{color:this.activecolor}:{}
  }

},
  }
</script>
<style>
  .tabbaritem{
  flex: 1;
  text-align: center;
  height: 50px;

}
.tabbaritem img{
  width: 24px;
  height: 26px;
}
/* 
:class='{active:isactive}'
.active{
  color: blue;
} */
</style>