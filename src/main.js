import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js'
import store from './store/index.js'
//自己创建的插件toast toast对象就是index.js的obj对象
import toast from './components/common/toast/index.js'

import FastClick  from 'fastclick' //解决移动端300ms延时
import VueLazyLoad from 'vue-lazyload' //图片懒加载,用户往下滑图片才会显示，省流量

Vue.config.productionTip = false
Vue.prototype.$bus=new Vue() //因为home 和homenavbar 和homenavbaritem 第一个和第三个不能直接通信要创建$bus

//安装自己创建的插件toasts
Vue.use(toast)

FastClick.attach(document.body)
Vue.use(VueLazyLoad)

// 图片懒加载方法：用了图片的地方把img :src='aaa[0]'改为 img v-lazy='aaa[0]'

new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
