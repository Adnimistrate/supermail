import { request } from "./request.js";

//gethomedata这是个函数，返回也是request的函数
//相当于两层
export function getbannersdata() {
  return request({
    //这里会拼接requser里面的url
    // url: "/home/multidata"
    url: "/getbannersdata"
  });
}

//请求推荐数据
export function getrecommendsdata() {
  return  request({
    url: "/getrecommendsdata"
  });
}

//请求商品1数据
export function getgoods1data() {
  return  request({
    url: "/getgoods1data"
  });
}

//请求商品2数据
export function getgoods2data() {
  return  request({
    url: "/getgoods2data"
  });
}

//请求商品3数据
export function getgoods3data() {
  return  request({
    url: "/getgoods3data"
  });
}


