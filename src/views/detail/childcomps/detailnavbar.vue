<template>
  <div class="detailnavbar">
  <navbar >
    <div slot="left" class="back" @click='back'>  <!-- 左边替换为返回按键 -->
      <img src="../../../assets/img/common/back.svg" alt="">
    </div>
    <div slot='center' class='title'>  <!-- 中间替换为文字 -->
      <div v-for='(item,index) in titles' class="titleitem"
      :class='{active:currentindex==index}' @click='itemclick(index)'>
      {{item}}
    </div>  <!-- 动态绑定active改变颜色 -->
    </div></navbar>

  </div>
  
</div>
</template>
<script>
  import navbar from '../../../components/common/navbar/navbar.vue'
  export default {
name:'detailnavbar',
components:{
  navbar,
},
data() {
  return {
    titles:['参数','商品','评论','推荐'],
    currentindex:0
  }
},
methods: {
  itemclick(index){
    this.currentindex=index
    this.$emit('titleclick',index)
  },
  back(){
    this.$router.back()  //router.back就是返回
  }
},
  }
</script>
<style>
  .detailnavbar img{
    margin-top: 3px;
  }
  .title{
    display: flex;
    padding: 3px 10px;
    
  }
  .titleitem{
    flex: 1;
    font-size: 13px;
  }
  .active{
    color: red;
  }
  .back{
    margin-top: 10px;
  }
</style>