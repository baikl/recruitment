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
        size = 10
        page = int(self.get_argument('page',0))
        count = wage.count()
        npage = count/size+1
        items = wage.page(page,size)
        self.render('admin/wage.html',page=page,npage=npage,wages=items)

@url(r'/admin/wage_edit')
class AdminWage_edit(BaseHandler):
    def get(self):
        self.render('admin/wage_edit.html')
    
    def post(self):
        starts = self.get_argument('start')
        ends = self.get_argument('end')
        wages = wage.insert(starts,ends)
        self.redirect('/admin/wage')


@url(r'/admin/wage/remove')
class Remove(BaseHandler):
    def get(self):
        _id = self.get_argument('_id')
        wage_rm=wage.remove(_id)
        self.redirect('/admin/wage')

@url(r'/admin/wage/alter')
class Alther(BaseHandler):
    def get(self):
        _id = self.get_argument('_id')
        item = wage.find_one(_id)
        self.render('admin/wage_add.html',item=item)

    def post(self):
        _id = self.get_argument('_id')
        start = self.get_argument('start')
        end = self.get_argument('end')
        wage_update = wage.update(_id,start=start,end=end)
        self.redirect('/admin/wage')

