from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from flask import Flask, render_template, flash, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 配置数据库地址
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root@127.0.0.1:3306/supermail'
# 关闭自动跟踪修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "12345678"


# 轮播图
class banners(db.Model):
    __tablename__ = 'banners'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(1000), nullable=False)
    # email = db.Column(db.String(50), nullable=False)
    # password = db.Column(db.String(256), nullable=False)


if __name__ == "__main__":
    db.drop_all()  # 删除原有表单，这个要重点注意，不然容易把别人的东西全删了，真的就从删库到跑路
    db.create_all()  # 创建表单

    k1 = banners(id='1', link='www.baidu.com', image='https://st-gdx.dancf.com/gaodingx/0/uxms/design/20200612-105308-8892.png?x-oss-process=image/resize,w_563/interlace,1,image/format,webp')
    k2 = banners(id='2', link='www.jd.com', image='https://st-gdx.dancf.com/gaodingx/0/uxms/design/20200527-100503-3f7a.png?x-oss-process=image/resize,w_563/interlace,1,image/format,webp')
    k3 = banners(id='3', link='http://localhost:8081/', image='https://st-gdx.dancf.com/gaodingx/0/uxms/design/20201103-115306-02b2.png?x-oss-process=image/resize,w_675/interlace,1,image/format,webp')
    k4 = banners(id='4', link='https://www.bilibili.com/video/BV15741177Eh?p=156', image='https://st-gdx.dancf.com/gaodingx/0/uxms/design/20200527-172041-e00e.png?x-oss-process=image/resize,w_563/interlace,1,image/format,webp')

    # 加载数据
    db.session.add_all([
        k1, k2, k3, k4
    ])
    db.session.commit()

    app.run(debug=True)
