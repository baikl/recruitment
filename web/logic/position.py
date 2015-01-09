#-*-coding:utf-8-*-

from bson import ObjectId
from kpages import get_context,mongo_conv
import category

TName='position'


def insert(name,title,ask,address,number,desc,job,education,date,**kwrags):
    coll=get_context().get_mongo()[TName]
    dct=dict(name=name,title=title,ask=ask,address=address,number=number,desc=desc,job=job,education=education,date=date)
    return coll.insert(dct)

def update(_id,**kwargs):
    coll= get_context().get_mongo()[TName]
    cond= dict(_id=ObjectId(_id))
    return coll.update(cond,{'$set':kwargs})

def count(**kwargs):
    coll = get_conetext().get_mongo()[TName]
    return coll.find(kwargs).count()

def page(page,size=5,**kwargs):
    coll= get_context().get_mongo()[TName]
    return coll.find(kwargs).skip(page*size).limit(size).sort('_id',-1)

def find_one(_id,**kwargs):
    coll=get_context().get_mongo()[TName]
    dct=dict(_id=ObjectId(_id))
    return coll.find_one(dct)
