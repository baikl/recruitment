# -*- coding:utf-8 -*-
"""
    index action demo
    author comger@gmail.com
"""
import tornado

from tornado import gen
from kpages import url, ContextHandler, LogicContext, get_context, service_async
from logic import user,category,position,company,genre,experience,wage,province #倒入logic里的user,new 
from logic.__init__ import BaseHandler

@url(r'/')
class IndexHandler(ContextHandler,tornado.web.RequestHandler):
    def get(self):
        size = 10
        page = int(self.get_argument('page',0))
        items = genre.page(page,size)
        count = genre.count()
        npage = count/size+1
        genre_page = genre.page(0,size=100)
        wage_page = wage.page(0,size=100)
        province_page = province.page(0,size=100)
        self.render('index.html',genres=genre_page,wages=wage_page,provinces=province_page,genre=items,page=page,npage=npage)


@url(r'/job')
class JobScreen(BaseHandler):
    def get(self):
        size = 10
        page = int(self.get_argument('page',0))
        items = genre.page(page,size)
        count = genre.count()
        npage = count/size+1
        genre_page = genre.page(0,size=100)
        wage_page = wage.page(0,size=100)
        province_page = province.page(0,size=100)
        self.render('job.html',genres=genre_page,wages=wage_page,provinces=province_page,genre=items,page=page,npage=npage)


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
        self.render('admin/job_add.html')

    def post(self):
        name=self.get_argument('name')
        title=self.get_argument('title')
        ask=self.get_argument('ask')
        address=self.get_argument('address')
        number=self.get_argument('number')
        desc=self.get_argument('desc')
        job=self.get_argument('job')
        education=self.get_argument('education')
        date=self.get_argument('date')
        _id=position.insert(name,title,ask,address,number,desc,job,education,date)
        self.redirect('/job/detail?_id='+str(_id))



@url(r'/job/detail')
class JobDetail(BaseHandler):
    def get(self):
        _id = self.get_argument('_id')
        positions = position.find_one(_id)
        self.render('information.html',item=positions)#

@url(r'/job/alter')
class Newsalter(BaseHandler):
    def get(self):
        self.render('admin/job_edit.html')#

    def post(self):
        self.redirect('/job/list')
