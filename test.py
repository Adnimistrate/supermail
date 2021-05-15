from flask import Flask, jsonify, request #新增jsonify处理json格式数据，request获取ajax前端发送来的参数。
from flask import render_template

app = Flask(__name__,
static_folder='./vue/dist/static',
template_folder = "./vue/dist")

@app.route('/')
def index():
  return render_template('index.html',name='index')

#定义api接口地址，和请求类型
@app.route('/api/login', methods=('GET', 'POST'))
def login():
  if request.method == 'POST':
    username = request.get_json().get('username') #获取ajax的参数
    password = request.get_json().get('password')
    return jsonify({'username': username,'password': password,'state':'success'}) #返回一个json格式的数据

if __name__ == '__main__':
  app.run()