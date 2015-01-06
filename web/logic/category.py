#-*-coding:utf-8-*-

from bson import ObjectId
from kpages import get_context,mongo_conv

TName ='category'


def insert(genre,province,wage,experience,**kwargs):
    coll = get_context().get_mongo()[TName]
    dct = dict(genre=genre,province=province,wage=wage,experience=experience)
    return coll.insert(dct)

def update(_id,**kwargs):
    coll = get_context().get_mongo()[TName]
    cond = dict(_id=ObjectId(_id))
    return coll.update(cond,{'$set':kwargs})

def page(page,size=10,**kwargs):
    coll = get_context().get_mongo()[TName]
    return coll.find(kwargs).skip(page*size).limit(size).sort('_id',-1)

def count(**kwargs):
    coll =get_context().get_mongo()[TName]
    return coll.find(kwargs).count()

def remove(_id,**kwargs):
    coll = get_context().get_mongo()[TName]
    dct= dict(_id=ObjectId(_id))
    return coll.remove(dct)

def find_one(_id,**kwargs):
    coll=get_context().get_mongo()[TName]
    dct=dict(_id=ObjectId(_id))
    return coll.find_one(dct)



