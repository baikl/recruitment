#-*-coding:utf-8-*-

from bson import ObjectId
from kpages import get_context,mongo_conv

TName = 'wage'

def insert (start,end,**kwargs):
    coll = get_context().get_mongo()[TName]
    dct = dict(start=start,end=end)
    return coll.insert(dct)

def count (**kwargs):
    coll = get_context().get_mongo()[TName]
    return coll.count(dct)

def update (_id,**kwargs):
    coll = get_context().get_mongo()[TName]
    dct = dict(_id = ObjectId(_id))
    return coll.update(dct)

def remove (_id,**kwargs):
    coll = get_context().get_mongo()[TName]
    dct = dict(_id=ObjectId(_id))
    return coll.remove(dct)

def find_one (_id,**kwargs):
    coll = get_context().get_mongo()[TName]
    dct = dict(_id=ObjectId(_id))
    return coll.find_one(dct)

