import axios from 'axios'

//简写省略promise因为本身返回的就是promise
export function request(config) {

  // 1.创建axios实例
  const instant1=axios.create({
    // baseURL:'http://123.207.32.32:8000',
    baseURL:'http://localhost:5000',
    timeout:5000
  })

    // 2.响应拦截器 
  instant1.interceptors.response.use(result=>{
    //去掉没用的东西，返回有用的东西 .data
    return result
  })

  //3.方送真正网络请求
 return instant1(config)
}







//   //2.axios请求拦截器 
//   instant1.interceptors.request.use(config=>{
// console.log(config);
// //用处？
// // 1.展示动画加载中...，携带信息，
// //拦了人家的config要还回去
// return config
//   })

