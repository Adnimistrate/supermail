from flask import Flask
import pymysql
import json
from flask_cors import CORS

import threading # 上锁的包

app = Flask(__name__)
CORS(app, resources=r'/*')

# 这是公共的数据库连接，所有线程共用一个连接池，需要考虑线程总数和连接池连接数上限的问题   
# 如果全部都同时连接这个公共的会不行
# 方法1.每个人都写一遍下面代码，都有自己的连接 方法二上锁 解决多个api同时请求防止多线程
# 创建数据库连接,password='root'
database = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           db='supermail',
                           charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = database.cursor()
# 创建锁
mutex=threading.Lock()

# 获取轮播图数据
@app.route('/getbannersdata/',methods=['GET','POST'])
def getbannersdata():   
    sql = 'select *from banners'
    mutex.acquire()  #上锁，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源
    cursor.execute(sql)
    mutex.release() #解锁
    data=cursor.fetchall()
    bannersdata = json.dumps(data)
    return bannersdata




#获取推荐图数据
@app.route('/getrecommendsdata/',methods=['GET','POST'])
def getrecommendsdata():
    sql = 'select *from recommends'
    mutex.acquire() 
    cursor.execute(sql)
    mutex.release()
    data=cursor.fetchall()
    recommendsdata = json.dumps(data)
    return recommendsdata


if __name__ == '__main__':
    app.run(host='localhost', port='5000', threaded=True, debug=True)
