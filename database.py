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


# 轮播图推荐图
class banners(db.Model):
    __tablename__ = 'banners'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(255), nullable=False)

# 推荐图


class recommends(db.Model):
    __tablename__ = 'recommends'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(10), nullable=False)


if __name__ == "__main__":
    db.drop_all()  # 删除原有表单，这个要重点注意，不然容易把别人的东西全删了，真的就从删库到跑路
    db.create_all()  # 创建表单

    b1 = banners(id='1', link='0', image='https://st-gdx.dancf.com/templets/70744/shots/20190823-095918-b6L_h.png?x-oss-process=image/resize,w_563/interlace,1,image/format,webp')
    b2 = banners(id='2', link='1', image='https://st-gdx.dancf.com/templets/74795/shots/20191216-174754-5SiJ8.png?x-oss-process=image/resize,w_563/interlace,1,image/format,webp')
    b3 = banners(id='3', link='2', image='https://st-gdx.dancf.com/gaodingx/0/uxms/design/20200728-170352-0ebb.png?x-oss-process=image/resize,w_563/interlace,1,image/format,webp')
    b4 = banners(id='4', link='3', image='https://st-gdx.dancf.com/gaodingx/0/uxms/design/20200703-175354-8e7a.png?x-oss-process=image/resize,w_563/interlace,1,image/format,webp')

    r5 = recommends(
        id='5', link='4', image='https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1398575065,2156416077&fm=26&gp=0.jpg', title='十点抢券')
    r6 = recommends(
        id='6', link='5', image='https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=143737326,3330500794&fm=26&gp=0.jpg', title='好物特卖')
    r7 = recommends(
        id='7', link='6', image='https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2118667908,3838752433&fm=26&gp=0.jpg', title='内购福利')
    r8 = recommends(
        id='8', link='7', image='https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4235146903,118695362&fm=26&gp=0.jpg', title='初秋上新')
    # 加载数据
    db.session.add_all([
        b1, b2, b3, b4
    ])

    db.session.add_all([
        r5, r6, r7, r8
    ])

    db.session.commit()

    app.run(debug=True)
