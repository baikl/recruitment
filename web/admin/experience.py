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


@url(r'/admin/experience')
class AdminExperience(BaseHandler):
    def get(self):
       # import pdb;pdb.set_trace()
        #_id = self.get_argument('_id')
        self.render('admin/experience.html')

@url(r'/admin/experience_edit')
class AdminExperience_edit(BaseHandler):
    def get(self):
        self.render('admin/experience_edit.html')
    

@url(r'/admin/remove')
class AdminRemove(BaseHandler):
    def get(self):
        self.render('')

@url(r'/admin/alter')
class AdminAlter(BaseHandler):
    def get(self):
        self.render('')

