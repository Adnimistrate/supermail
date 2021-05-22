import toast from './toast.vue'
//封装思想
//main.js过来后会自动执行obj.install函数
//相当于创建一个div组件
const obj={}
obj.install=function(Vue){
  //1.创建组件构造器
  const toastcontrustor=Vue.extend(toast)

  //2.new的方式，根据组件构造器，可以创建出来一个组件对象
  const toasts=new toastcontrustor()

  //3将组件对象，手动挂载到某一个元素上
  toasts.$mount(document.createElement('div'))

  //4.toast.$el对应的就是div
  document.body.appendChild(toasts.$el)
  Vue.prototype.$toast=toasts

}
export default obj