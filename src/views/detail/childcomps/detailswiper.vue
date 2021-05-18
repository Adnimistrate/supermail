<template>

    <Swiper class="detailswiper" >
      <SwiperItem v-for='item in detaildata' >
        <img :src="item[2]" alt="">
      </SwiperItem>
    </Swiper>

</template>
<script>
  import {Swiper,SwiperItem} from '../../../components/common/swiper/index.js'
  export default {
name:'detailswiper',
props:{
  detaildata:{
    type:Array,
    default(){
      return[]
    }
  }

},
components:{
  Swiper,
  SwiperItem
}
  }
</script>
<style>
  .detailswiper{
    padding-top: 15px;
    height: 350px;

    width: 100%;
    overflow: hidden;
  }

  .detailswiper img{
    width: 100%;
    height: 100%;
  }

</style>