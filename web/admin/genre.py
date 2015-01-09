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
       # import pdb;pdb.set_trace()
       # _id = self.get_argument('_id')
       # genres = genre.find_one(_id)
        self.render('admin/genre.html')

@url(r'/admin/genre_edit')
class AdminGenre_edit(BaseHandler):
    def get(self):
        self.render('admin/genre_edit.html')
    
   # def post(self):
       # title = self.get_argument('title')
       # _id = genre.insert(title)
        #self.redirect('/listname?_id'+str(_id))
       # import pdb;pdb.set_trace()

@url(r'/admin/remove')
class Province(BaseHandler):
    def get(self):
        self.render('')

@url(r'/admin/alter')
class Wage(BaseHandler):
    def get(self):
        self.render('')

