
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
        self.render('admin/listname_add.html')
    
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
        self.render('admin/listname_edit.html',item=item)#

    def post(self):
        _id=self.get_argument('_id')
        genre=self.get_argument('genre')
        prov=self.get_argument('province')
        wage=self.get_argument('wage')
        experi=self.get_argument('experience')
        categorys=category.update(_id,genre=genre,prov=prov,wage=wage,experi=experi)
        self.redirect('/listname')
