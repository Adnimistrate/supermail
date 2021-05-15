<template>
    <div class="slide">
      <!-- //预留插超home里面插入图片 -->
      <slot></slot>
    </div>
</template>

<script>
	export default {
		name: "SwiperItem"
	}
</script>

<style scoped>
  /* //限定里面item的大小，而swiper.vue是搭建整个轮播图框架 */
  .slide {
    width: 100%;
    flex-shrink: 0;
  }

  .slide img {
    width: 100%;
  }
</style>
