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


@url(r'/admin/province')
class Province(BaseHandler):
    def get(self):
       # import pdb;pdb.set_trace()
       # _id = self.get_argument('_id')
        self.render('admin/province.html')

@url(r'/admin/province_edit')
class Province_edit(BaseHandler):
    def get(self):
        self.render('admin/province_edit.html')
    

@url(r'/admin/alter')
class ProvinceAlter(BaseHandler):
    def get(self):
        self.render('')

@url(r'/admin/remove')
class ProvinceRemove(BaseHandler):
    def get(self):
        self.render('')

