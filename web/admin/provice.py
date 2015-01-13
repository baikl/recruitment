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
        size = 10
        page = int(self.get_argument('page',0))
        count = province.count()
        npage = count/size+1
        items = province.page(page,size)
        self.render('admin/province.html',page=page,npage=npage,provinces=items)

@url(r'/admin/province_edit')
class Province_edit(BaseHandler):
    def get(self):
        self.render('admin/province_edit.html')

    def post(self):
        title = self.get_argument('province')
        provinces = province.insert(title)
        self.redirect('/admin/province')
    

@url(r'/admin/province/alter')
class ProvinceAlter(BaseHandler):
    def get(self):
        _id = self.get_argument('_id')
        item = province.find_one(_id)
        self.render('admin/province_add.html',item=item)

    def post(self):
        _id = self.get_argument('_id')
        title = self.get_argument('province')
        province_update = province.update(_id,title=title)
        self.redirect('/admin/province')


@url(r'/admin/province/del')
class ProvinceRemove(BaseHandler):
    def get(self):
        _id = self.get_argument('_id')
        prov_rm = province.remove(_id)
        self.redirect('/admin/province')

