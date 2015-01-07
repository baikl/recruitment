# -*- coding:utf-8 -*-


import tornado

from tornado import gen
from kpages import url, ContextHandler, LogicContext, get_context, service_async
from logic import user,category,position,company #倒入logic里的user,new 

class BaseHandler(ContextHandler,tornado.web.RequestHandler):
    uid = property(lambda self:self.get_cookie('uid'))#基类uid(接受cookie里的uid)

    def prepare(self):
        if not self.uid:#如果没有登录,则将弹到登录页面
            self.redirect('/user/login')
