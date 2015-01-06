#-*-coding:utf-8-*-

from bson import ObjectId
from kpages import get_context,mongo_conv

TName='company'

def insert(name,intr,proper,indu,scale,area,address,website,contant,phone,email):
    coll=get_context.get_mongo()[TName]
    dct=dict(name=name,intr=intr,proper=proper,indu=indu,scale=scale,area=area,address=address,website=wbsite,contant=contant,phone=phone,email=email)
    return coll.insert(dct)

def update(_id,**kwargs):
    coll= get_context.get_mongo()[TName]
    cond= dict(_id=ObjectId(_id))
    return coll.update(cond,{'$set':kwargs})

def count(**kwargs):
    coll=get_context().get_mongo()[TName]
    return coll.find(kwargs).count()

def find_one(_id,**kwargs):
    coll=get_context().get_mongo()[TName]
    return coll.find_one(dct)
