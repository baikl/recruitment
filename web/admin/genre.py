# -*- coding:utf-8 -*-

"""
    Filename: listname.py
    Author: baikl@smartbow.net
"""

import tornado

from tornado import gen
from kpages import url,ContextHandler,LogicContext,get_context,service_async
from logic import user,category,position,company,genre,experience,wage,province
from logic.__init__ import BaseHandler


@url(r'/admin/genre')
class AdminGenre(BaseHandler):
    def get(self):
        size = 10
        page = int(self.get_argument('page',0))
        items = genre.page(page,size)
        count = genre.count()
        npage = count/size+1
       # import pdb;pdb.set_trace()
        self.render('admin/genre.html',genres=items,page=page,npage=npage)

@url(r'/admin/genre_edit')
class AdminGenre_edit(BaseHandler):
    def get(self):
        self.render('admin/genre_edit.html')
    
    def post(self):
        title = self.get_argument('genre')
        genres = genre.insert(title)
        self.redirect('/admin/genre')

@url(r'/admin/genre/del')
class Province(BaseHandler):
    def get(self):
        genre_id = self.get_argument('_id')
        genres= genre.remove(genre_id)
        self.redirect('/admin/genre')

@url(r'/admin/genre/alter')
class Wage(BaseHandler):
    def get(self):
        #import pdb;pdb.set_trace()
        _id = self.get_argument('_id')
        item = genre.find_one(_id)
        self.render('admin/genre_add.html',item=item)
        #import pdb;pdb.set_trace()
    
    def post(self):
        _id = self.get_argument('_id')
        title = self.get_argument('genre')
        genres = genre.update(_id,title=title)
        self.redirect('/admin/genre')
