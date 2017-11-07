#coding=utf8
'''
Created on 2017年11月7日
@author: 李超
'''
from flask import Flask
from flask import render_template
from flask import request
from web02 import forms

app = Flask(__name__)

@app.route('/login',methods = ['GET' , 'POST'])
def login():
    #接收参数
    form = forms.LoginForm()
    #提交验证
    if request.method == 'POST':
        if form.validate_on_submit(request.form['username'],request.form['password']):
            #打印(ps:验证逻辑自行补上)
            print('username:' + request.form['username'] + ',password:' + request.form['password'])
            #返回到index.html页面
            return render_template('index.html',username = request.form['username'])
    #未提交
    return render_template('login.html',form = form)

if __name__=='__main__':
    app.run('0.0.0.0',8888,True)

