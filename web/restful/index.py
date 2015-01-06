# -*- coding:utf-8 -*-
"""
    index action demo
    author comger@gmail.com
"""
import tornado

from tornado import gen
from kpages import url, ContextHandler, LogicContext, get_context, service_async
from logic import user,category,position,company #倒入logic里的user,new 

class BaseHandler(ContextHandler,tornado.web.RequestHandler):
    uid = property(lambda self:self.get_cookie('uid'))#基类uid(接受cookie里的uid)

    def prepare(self):
        if not self.uid:#如果没有登录,则将弹到登录页面
            self.redirect('/user/login')


@url(r'/user/insert')
class UserInsertHandler(tornado.web.RequestHandler):
    def get(self):#渲染一个插入名字和密码注册的页面
         self.render('reg.html')
        
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
        self.render('login.html')

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
    

@url(r'/')
class IndexHandler(ContextHandler,tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

@url(r'/job')
class JobScreen(BaseHandler):
    def get(self):
        self.render('job.html')


@url(r'/job/list')
class NewsList(BaseHandler):
    def get(self):
        size = 10
        page = int(self.get_argument('page',0))
        count = category.count()
        npage = count/size+1
        items = position.page(0,size=100)
        self.render('job_list.html',campany=items,page=page,npage=npage)
    

@url(r'/job/edit')
class JobEdit(BaseHandler):
    def get(self):
        self.render('job_add.html')

    def post(self):
       # name=self.get_argument('name')
       # ask=self.get_argument('ask')
       # address=self.get_argument('address')
       # number=self.get_argument('number')
       # desc=self.get_argument('desc')
       # date=self.get_argument('date')
       # company=company.insert(name,ask,address,number,desc,date)
        self.redirect('/job/detail')



@url(r'/job/detail')
class JobDetail(BaseHandler):
    def get(self):
        self.render('information.html')#

@url(r'/job/firm')
class JobFirm(BaseHandler):
    def get(self):
        self.render('company.html')#

@url(r'/job/addcom')
class Jobaddcom(BaseHandler):
    def get(self):
        self.render('company_edit.html')#

@url(r'/job/positions')
class Jobaddcm(BaseHandler):
    def get(self):
        self.render('company_edit.html')#

@url(r'/job/alter')
class Newsalter(BaseHandler):
    def get(self):
        self.render('job_edit.html')#

    def post(self):
        self.redirect('/job/list')
    

@url(r'/listname')
class ListName(BaseHandler):
    def get(self):#
        size = 10
        page = int(self.get_argument('page',0))
        items = category.page(page,size)
        count =category.count()
        npage = count/size+1

        self.render('listname.html',category=items,page=page,npage=npage)

@url(r'/listname_add')
class Listname_add(BaseHandler):
    def get(self):
        self.render('listname_add.html')
    
    def post(self):
        genre=self.get_argument('genre')
        prov=self.get_argument('province')
        wage=self.get_argument('wage')
        experi=self.get_argument('experience')
        categorys=category.insert(genre,prov,wage,experi)
        self.redirect('/listname')



@url(r'/listname/alter')
class Listnamealter(BaseHandler):
    def get(self):
        _id= self.get_argument('_id')
        item=category.find_one(_id)
        self.render('listname_edit.html',item=item)#

    def post(self):
        _id=self.get_argument('_id')
        genre=self.get_argument('genre')
        prov=self.get_argument('province')
        wage=self.get_argument('wage')
        experi=self.get_argument('experience')
        categorys=category.update(_id,genre=genre,prov=prov,wage=wage,experi=experi)
        self.redirect('/listname')



    

