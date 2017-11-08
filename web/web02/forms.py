#coding=utf8
'''
Created on 2017年11月7日
@author: 李超
'''

import MySQLdb
from wtforms import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required 

class LoginForm(Form):
    username = TextField('username',validators = [Required()])
    password = PasswordField('password',validators = [Required()])

    def validate_on_submit(self,uname,pwd):
        conn = MySQLdb.connect('127.0.0.1','root','1234','test')
        cur = conn.cursor()
        sql = 'select * from p_user where uname=%s and pwd=%s'
        cur.execute(sql,(uname,pwd))
        print uname, pwd
        result = cur.fetchone()
        cur.close()
        conn.close()
        
        return result
