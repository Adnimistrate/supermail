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

export function getproductdata(iid) {
  return request({
    url: "/getproductdata/",
    params:{
      iid:iid
    }
  });
}


export function getproductinfodata(iid) {
  return request({
    url: "/getproductinfodata/",
    params:{
      iid:iid
    }
  });
}

export function getproductmarkdata(iid) {
  return request({
    url: "/getproductmarkdata/",
    params:{
      iid:iid
    }
  });
}

export function getgoodsrecommanddata(iid) {
  return request({
    url: "/getgoodsrecommanddata/",
    params:{
      iid:iid
    }
  });
}