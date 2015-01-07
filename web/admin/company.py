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
        self.render('company.html')#


@url(r'/job/addcom')
class Jobaddcom(BaseHandler):
    def get(self):
        self.render('admin/company_edit.html')#

    def post(self):
        name=self.get_argument('name')
        intr=self.get_argument('intr')
        proper=self.get_argument('proper')
        indu=self.get_argument('indu')
        scale=self.get_argument('scale')
        area=self.get_argument('area')
        address=self.get_argument('address')
        website=self.get_argument('website')
        contant=self.get_argument('contant')
        phone=self.get_argument('phone')
        email=self.get_argument('email')
        company=company.insert(name,intr,proper,indu,scale,area,address,website,contant,phone,email)
        self.redirect('/job/firm')

@url(r'/job/positions')
class Jobaddcm(BaseHandler):
    def get(self):
        self.render('admin/company_edit.html')#

@url(r'/job/alter')
class Newsalter(BaseHandler):
    def get(self):
        self.render('admin/job_edit.html')#

    def post(self):
        self.redirect('/job/list')
    