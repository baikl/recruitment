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


@url(r'/admin/wage')
class ListName(BaseHandler):
    def get(self):
       # import pdb;pdb.set_trace()
        #_id = self.get_argument('_id')
        self.render('admin/wage.html')

@url(r'/admin/wage_edit')
class AdminWage_edit(BaseHandler):
    def get(self):
        self.render('admin/wage_edit.html')
    

@url(r'/admin/remove')
class Remove(BaseHandler):
    def get(self):
        self.render('')

@url(r'/admin/alter')
class Alther(BaseHandler):
    def get(self):
        self.render('')

