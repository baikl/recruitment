# -*- coding:utf-8 -*-
"""
    index action demo
    author comger@gmail.com
"""
import tornado

from tornado import gen
from kpages import url, ContextHandler, LogicContext, get_context, service_async
from logic import user,category,position,company #倒入logic里的user,new



@url(r'/user/insert')
class UserInsertHandler(tornado.web.RequestHandler):
    def get(self):#渲染一个插入名字和密码注册的页面
         self.render('admin/reg.html')
        
    def post(self):#判断插入的名字和密码是否以存在   如果存在则注册失败
        username = self.get_argument('email')#获取一个email的的参数
        pwd = self.get_argument('pwd')
        again_pwd = self.get_argument('again_pwd')
        
        if pwd==again_pwd:#如果pwd和again_pwd完全相同,则将插入到数据表里,否则返回'密码不一致'
            va=user.insert(username,pwd)
            if va == False:#如果你输入的va值和数据表里有相同的则返回'用户名以存在'
                self.write('用户名以存在')
            else:
                self.redirect('/user/login')#如果上面为True则弹出登录页面

        else:
            self.write('输入密码不一致')


@url(r'/user/login')
class LoginHandler(ContextHandler,tornado.web.RequestHandler):
    def get(self):#渲染一个有名字和密码的登录页面
        name=self.get_cookie('uid')#获取cookie的uid
        self.render('admin/login.html')

    def post(self):#获取名字和密码并查询名字和密码是否对应
        username = self.get_argument('name',None)#获取用户名和密码
        pwd = self.get_argument('pwd',None)
        val = user.login(username,pwd)#查询获取的内容和表里的内容是否一致
        if not val:#如果内容不一致,则返回密码错误,否则弹出带有uid的新闻列表
            self.write('密码错误')
        else:                                 
            self.set_cookie("uid",username)
            self.redirect('/job')
          #print val #如果密码错则返回None   否则返回一个字典
    








    

