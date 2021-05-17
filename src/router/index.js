import Vue from 'vue'
import VueRouter from 'vue-router'

//懒加载,就是打包多个js加快访问速度
const Home=()=>import('../views/home/Home.vue')
const Category=()=>import('../views/category/Category.vue')
const Cart=()=>import('../views/cart/Cart.vue')
const Profile=()=>import('../views/profile/Profile.vue')
const Detail=()=>import('../views/detail/detail.vue')

//1.通过Vue.use(插件)，安装插件
Vue.use(VueRouter)

const routes=[
  {
    path:'',
    redirect:'/Home'
  },
  {
    path:'/Home',
    component:Home
  },
  {
    path:'/Category',
    component:Category
  },
  {
    path:'/Cart',
    component:Cart
  },
  {
    path:'/Profile',
    component:Profile
  },
  {
    path:'/detail/:iid', //要传参数加:aaa
    component:Detail
  },
]

//配置路由和组件之间的应用关系
const router=new VueRouter({

  routes,
  mode:'history'  //链接会更好看
})

export default router