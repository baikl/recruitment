# -*- coding:utf-8 -*-
"""
    index action demo
    author comger@gmail.com
"""
import tornado

from tornado import gen
from kpages import url, ContextHandler, LogicContext, get_context, service_async
from logic import user,category,position,company #倒入logic里的user,new 
from logic.__init__ import BaseHandler

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
        self.render('admin/job_add.html')

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

@url(r'/job/alter')
class Newsalter(BaseHandler):
    def get(self):
        self.render('admin/job_edit.html')#

    def post(self):
        self.redirect('/job/list')
