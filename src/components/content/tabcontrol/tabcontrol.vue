<template>
  <!-- //这是公共的组件，别人也要用，可以用插超，
    用插超是比较复杂时候，仅仅是文字不一样可以不用 -->
  <div class="tabcontrol">
    <div v-for="(item,index) in titles" 
    class="tabcontrolitem" :class="{active:index==currentindex}"   
    @click='itemclick(index)' >    <!--绑定class,在..条件下使用active的样式-->
<!--监听index点击改变currentindex-->



    <!--整个大的盒子包装一个div,每个div包个span，就可以设置每个的样式-->
      <span>
        {{ item }}
      </span>
    </div>
  </div>
</template>
<script>
export default {
  name: "tabcontrol",
  props: {
    //不用插超可以通过priops决定上面显示几个文字
    titles: {
      type: Array,
      default() {
        return [];
      }
    }
  },
  data() {
    return {
      currentindex:0 //默认第一个激活
    }
  },
  methods: {
    itemclick(index){
      this.currentindex=index
      this.$emit('tabclick',index)  //子组件传给父组件知道点了哪个
    }
  },
};
</script>
<style>
  .tabcontrol{
    display: flex;  /* 总体flex布局 */
    text-align: center;
    font-size: 15px;
    background-color: #fff;
  }
  .tabcontrolitem{
    flex: 1;  /* 总体平分 */
    height: 40px;  /* 靠文字撑起太低了，直接设置高度 */
    line-height: 40px; /* 进一步撑起防止... */
  }
  .tabcontrolitem span{
    padding: 5px;  /* 撑起线和文字的距离 */
  }
  .active span{
    color: cyan;   /* 文字和下划线都要颜色 */
    border-bottom: 3px solid cyan; /* 下划线只要文字这么长，所以加在span上面 */
  }
</style>
