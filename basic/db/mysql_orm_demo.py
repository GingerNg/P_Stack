#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
https://www.cnblogs.com/pycode/p/mysql-orm.html
SQLAlchemy--> pymysql--> mysql
'''
# http://www.jb51.net/article/118715.htm   Flask-sqlalchemy

from sqlalchemy import create_engine
'''
底层处理
'''
#创建引擎
engine = create_engine(
    "mysql+pymysql://root:XXXX@127.0.0.1:3306/test?charset=utf8", max_overflow=5, encoding='utf-8')

def underlying():  
    #执行sql语句
    engine.execute('INSERT INTO people (name,age) values (%s, %s)', ['mike', '1'])

    result = engine.execute('select * from people')
    res = result.fetchall()
    print(res)

'''
orm功能使用
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()

# 创建单表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

# 一对多
class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    # 外键 如果一个实体的某个字段(主表)指向另一个实体(从表)的主键，就称为外键被指向的实体 https://www.cnblogs.com/zunpeng/p/3878459.html
    favor_id = Column(Integer, ForeignKey("favor.nid"))

# 多对多
class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)

Base.metadata.create_all(engine)  # 创建表
# Base.metadata.drop_all(engine)   #删除表

'''
CRUD
'''
Session = sessionmaker(bind=engine)
session = Session()

obj = Users(name="alex0", extra='sb')
session.add(obj)
session.add_all([
    Users(name="alex1", extra='sb'),
    Users(name="alex2", extra='sb'),
])
session.commit()

class Role(Base):
    __tablename__ = 'role'
    rid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)

class User1(Base):
    __tablename__ = 'user1'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    role = Column(Integer, ForeignKey('role.rid'))
    group = relationship("Role", backref='uuu')  # Role为类名

    def __repr__(self):   # <==> Java中的toString()方法 
        output = "(%s,%s,%s)" % (self.nid, self.name, self.role)
        return output

Base.metadata.create_all(engine)  # 创建表


def main():
    session.add_all([
        Role(rid=124,name='student'),
        Role(rid=123,name='teacher'),
    ])
    session.add_all([
        User1(nid=12, name="alex1", role=124),
        User1(nid=123,name="alex2", role=123),
    ])
    # session.flush()
    session.commit()
    res = session.query(User1).all()
    print(res)
    '''
    事务: flush就是把客户端尚未发送到数据库服务器的SQL语句发送过去，commit就是告诉数据库服务器提交事务。
    commit之后其它session可查看到相同的内容,如果只flush或者不操作,则其它session看不到变更的内容

    多个事务可以获取共享锁, 互斥锁只能一个事务获取
    悲观锁：在读取数据时锁住那几行，其他对这几行的更新需要等到悲观锁结束时才能继续 
    乐观所：读取数据时不锁，更新时检查是否数据已经被更新过，如果是则取消当前更新
    MVCC--多版本并发控制，同一个数据有多个版本，事务开启时看到是哪个版本就看到这个版本，最大的好处是读写不冲突，只有写于写是冲突的，这个特性可以很大程度上提升性能
    '''
    try:
        user = session.Query(User1).first()
        user.role = 1234
        session.commit()
    except:
        session.rollback() 
        print ("rollback")
  


if __name__ == '__main__':
    main()
