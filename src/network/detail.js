import { request } from "./request.js";


export function getdetailsdata(iid) {
  return request({
    url: "/getdetailsdata/",
    params:{
      iid:iid
    }
  });
}

export function getgoodsinfo(iid) {
  return request({
    url: "/getgoodsinfo/",
    params:{
      iid:iid
    }
  });
}

export function getshopdata(iid) {
  return request({
    url: "/getshopdata/",
    params:{
      iid:iid
    }
  });
}