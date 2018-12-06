#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
事务-->  分布式事务  http://blog.jobbole.com/95632/
 一般事务控制: begin--> commit
 
 二阶段提交, Two - Phase, 是为解决分布式环境下多点事务控制的一套协议.
 请求提交--> 提交  
 从多点事务的控制来看, 应用层要做的事是, 先把任务分发出去, 然后收集"事务准备"的状态(prepare transaction 的结果). 根据收集的结果决定最后是 commit 还是 rollback .
 
 三阶段:
 请求提交--> 预提交--> 提交
 相比于二阶段: 减少阻塞 但是可能存在数据不一致的情况
 '''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:XXX@127.0.0.1:3306/test?charset=utf8", max_overflow=5, encoding='utf-8')
engine1 = create_engine(
    "mysql+pymysql://root:XXXX@127.0.0.1:3306/test?charset=utf8", max_overflow=5, encoding='utf-8')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

def two_phase():
    Session = sessionmaker(twophase=True)
    Session = sessionmaker(twophase=True)
    Session.configure(binds={User: engine, Blog: engine1})
    session = Session()
    obj = User(name="alex-d", extra='sb')
    session.add(obj)
    session.commit()

def main():
    two_phase()

if __name__ == '__main__':
    main()
