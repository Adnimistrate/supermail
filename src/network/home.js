import { request } from "./request.js";

//gethomedata这是个函数，返回也是request的函数
//相当于两层
export function gethomedata() {
  return request({
    //这里会拼接requser里面的url
    // url: "/home/multidata"
    url: "/getbannersdata"
  });
}
