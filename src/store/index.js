import Vue from 'vue'
import Vuex from 'vuex'


// 1.安装插件
Vue.use(Vuex)

// 2.创建store对象
const store=new Vuex.Store({
  state:{
    shopcart:[]
  },
  mutations:{
    addnum(state,products){
      state.shopcart.push(products) //新商品添加到shopcar
      },
  },
  actions:{
    //只有在action里面才能用prmise因为是异步请求
    addtocart(context,newproducts){
      //返回promise可以使用resolve传递信息给前台，前台detail.js用.then可以拿到信息
      return   new Promise((resolve, reject) => {
      //products新添加的商品，如果里面有就加数量，不然，shopcar数组才添加这个商品
      let oldproduct=null;
      for(let item of context.state.shopcart){
        if(item.iid==newproducts.iid){
          oldproduct=item
        }
      }
      //判断oldproduct有数据原来加1否在添加新商品
      if(oldproduct){
        oldproduct.count+=1  //因为是旧商品之前已经添加了count属性直接加1就行了
        context.commit('addnum',oldproduct)
        resolve('当前商品数量+1')
      }
      else{
        newproducts.count=1  //新商品添加conut属性同时赋值1
        newproducts.checked=true //商品默认是否被选中
        context.commit('addnum',newproducts)
        // state.shopcart.push(newproducts) //新商品添加到shopcar
        resolve('添加了新的商品')
      }
    })
    }
  }
})
export default store