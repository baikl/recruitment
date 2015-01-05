#-*-coding:utf-8-*-
#Filename:user.py
"""
    author baikl
    Functions
"""
from kpages import get_context

TName = 'user'

def insert(username,pwd,**kwargs):
    
    coll = get_context().get_mongo()[TName]
    if coll.find_one(dict(username=username)):
        return False

    dct = dict(username=username,pwd=pwd)
    return coll.insert(dct)

def login(username,pwd):
    coll = get_context().get_mongo()[TName]

    return coll.find_one(dict(username=username,pwd=pwd))

