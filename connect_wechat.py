from flask import Flask
import pymysql
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')

# 创建数据库连接,password='root'
database = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           db='supermail',
                           charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = database.cursor()


# 获取轮播图数据
@app.route('/getbannersdata/',methods=['GET','OPTIONS'])
def getbannersdata():
    sql = 'select *from banners'
    cursor.execute(sql)
    result = cursor.fetchall()
    fields = cursor.description
    # 定义字段名的列表
    column_list = []
    json_list = []
    for i in fields:
        # 提取字段名，追加到列表中
        column_list.append(i[0])
    # # 打开输出结果文件
    # # with open('../data/json.txt', 'w+') as f:
    #     # 一次循环，row代表一行，row以元组的形式显示
    for row in result:
        # 定义Python 字典
        data = {}
        # 将row中的每个元素，追加到字典中。
        for i in range(len(column_list)):
            data[column_list[i]] = row[i]
        json_list.append(data)
        imagedata = json.dumps(json_list, ensure_ascii=False)
    return imagedata


if __name__ == '__main__':
    app.run(host='localhost', port='5000', threaded=True, debug=True)
