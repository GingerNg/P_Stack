# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: sqlalchemy_demo.py
@time: 2018/9/18 18:54
"""

"""
Dialect--方言
https://www.cnblogs.com/zhangxinqi/p/8480049.html

"""

from sqlalchemy import create_engine, desc, func, and_


def exec_sql():

    #创建引擎
    engine = create_engine("mysql+pymysql://root:XXX@X.X.X.X:8011/datastorage", max_overflow=5)
    #执行sql语句
    # engine.execute("INSERT INTO user (name) VALUES ('dadadadad')")

    result = engine.execute('select * from store_datainfo')
    res = result.fetchall()
    print(res[0])


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://XXX:XXX@X.X.X.X:8011/clean_resultdb", max_overflow=5)

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

Base.metadata.create_all(engine)  #创建表
# Base.metadata.drop_all(engine)   #删除表

if __name__ == "__main__":
    obj = Users(name="alex0", extra='sb')
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    增
    """
    # session.add(obj)
    # session.add_all([
    #     Users(name="alex1", extra='sb'),
    #     Users(name="alex2", extra='sb'),
    # ])
    # session.commit()  # 提交

    """删除"""
    session.query(Users).filter(Users.id > 7).delete()
    session.commit()

    """修改"""
    session.query(Users).filter(Users.id == 3).update({'name':'feng','extra':"bs"})
    session.commit()

    """
    查
    查询方式总结
    https://my.oschina.net/freegeek/blog/222725
    """
    print(session.query(Users).filter_by(extra='sb').all())

    print(session.query(Users).filter(Users.name == "user").all())

    query = session.query(Users).order_by(Users.name).limit(4)
    print([result.extra for result in query])

    print(session.query(Users).filter(Users.extra == 'sb').all())

    # 多条件查询
    print(session.query(Users).filter(and_(Users.name.like("alex%"), Users.extra=="bb")).all())

    ret = session.query(Users).filter(Users.extra.in_(['sb', 'bb'])).all()  # 可用
    print(ret)
    # ret = session.query(Users.name('name_label')).all()
    # print(ret,type(ret))

    # ret = session.query(User).order_by(User.id).all()
    # print(ret)

    # ret = session.query(User).order_by(User.id)[1:3]