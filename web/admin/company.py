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

@url(r'/job/firm')
class JobFirm(BaseHandler):
    def get(self):
        _id = self.get_argument('_id')
        companys = company.find_one(_id)
        self.render('admin/company.html',item=companys)#


@url(r'/job/addcom')
class Jobaddcom(BaseHandler):
    def get(self):
        self.render('company_edit.html')#

    def post(self):
        name = self.get_argument('name')
        intr = self.get_argument('intr')
        proper = self.get_argument('proper')
        indu = self.get_argument('indu')
        scale = self.get_argument('scale')
        area = self.get_argument('area')
        address = self.get_argument('address')
        website = self.get_argument('website')
        contant = self.get_argument('contant')
        phone = self.get_argument('phone')
        email = self.get_argument('email')
        _id= company.insert(name,intr,proper,indu,scale,area,address,website,contant,phone,email)
        self.redirect('/job/firm?_id='+str(_id))

@url(r'/job/positions')
class Jobaddcm(BaseHandler):
    def get(self):
        self.render('positions.html')#

    
