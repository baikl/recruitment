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
        size = 10
        page = int(self.get_argument('page',0))
        count = experience.count()
        npage = count/size+1
        items = experience.page(page,size)
        self.render('admin/experience.html',page=page,npage=npage,experiences=items)

@url(r'/admin/experience_edit')
class AdminExperience_edit(BaseHandler):
    def get(self):
        self.render('admin/experience_edit.html')
    
    def post(self):
        starts = self.get_argument('start')
        ends = self.get_argument('end')
        experiences= experience.insert(starts,ends)
        self.redirect('/admin/experience')

@url(r'/admin/experience/remove')
class AdminRemove(BaseHandler):
    def get(self):
        _id = self.get_argument('_id')
        experi_rm = experience.remove(_id)
        self.redirect('/admin/experience')

@url(r'/admin/experience/alter')
class AdminAlter(BaseHandler):
    def get(self):
        _id = self.get_argument('_id')
        item = experience.find_one(_id)
        self.render('admin/experience_add.html',item=item)

    def post(self):
        _id = self.get_argument('_id')
        start = self.get_argument('start')
        end = self.get_argument('end')
        experi_update = experience.update(_id,start=start,end = end)
        self.redirect('/admin/experience')

