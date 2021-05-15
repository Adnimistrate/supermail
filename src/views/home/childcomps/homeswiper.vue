<template>
  <!-- //继续封装，home里面太多东西，变成子组件 -->
  <Swiper>
    <!-- //不知道有多少个，通过遍历拿到自动决定轮播图个数 -->
    <SwiperItem v-for="item in banners">
      <a :href="item.link">
        <img :src="item.image" alt="" />
      </a>
    </SwiperItem>
  </Swiper>
</template>
<script>
import { Swiper, SwiperItem } from "../../../components/common/swiper/index.js";
export default {
  name: "homeswiper",
  components: {
    Swiper,
    SwiperItem
  },
  //用props拿父组件数据,限制类型和设置默认值 props[a{},b{}]
  props:{
    banners:{
      type:Array,
      default(){
        return []
      }
    }
  
}
};
</script>
<style></style>
