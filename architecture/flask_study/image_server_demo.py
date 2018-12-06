#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: mongodb_demo.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-29 下午8:08
 @desc:
 http://www.jb51.net/article/60738.htm

 MIME(Multipurpose Internet Mail Extensions)多用途互联网邮件扩展类型。
 是设定某种扩展名的文件用一种应用程序来打开的方式类型

304:
 https://www.cnblogs.com/ziyunfei/archive/2012/11/17/2772729.html
 https://segmentfault.com/a/1190000004084801
"""
import hashlib
import datetime
import flask
import pymongo
import bson.binary
import bson.objectid
import bson.errors
from cStringIO import StringIO
from PIL import Image
app = flask.Flask(__name__)
app.debug = True
db = pymongo.MongoClient('localhost', 27017).test
allow_formats = set(['jpeg', 'png', 'gif'])

def save_file(f):
  content = StringIO(f.read())
  try:
    mime = Image.open(content).format.lower()  # 后缀
    if mime not in allow_formats:
      raise IOError()
  except IOError:
    flask.abort(400)
  sha1 = hashlib.sha1(content.getvalue()).hexdigest()
  c = dict(
    content=bson.binary.Binary(content.getvalue()),
    mime=mime,
    time=datetime.datetime.utcnow(),
    sha1=sha1,
  )
  try:
    db.files.save(c)
  except pymongo.errors.DuplicateKeyError:
    pass
  return sha1



@app.route('/f/<sha1>')
def serve_file(sha1):
  try:
    f = db.files.find_one({'sha1': sha1})
    if f is None:
      raise bson.errors.InvalidId()
    if flask.request.headers.get('If-Modified-Since') == f['time'].ctime():
      return flask.Response(status=304)
    resp = flask.Response(f['content'], mimetype='image/' + f['mime'])
    resp.headers['Last-Modified'] = f['time'].ctime()
    return resp
  except bson.errors.InvalidId:
    flask.abort(404)

@app.route('/upload', methods=['POST'])
def upload():
  f = flask.request.files['uploaded_file']  #  flask.request.files[KEY] 获取上传文件对象, KEY 为页面 form 中 input 的 name 值
  sha1 = save_file(f)
  return flask.redirect('/f/' + str(sha1))  # 重定向

@app.route('/')
def index():
  return '''
  <!doctype html>
  <html>
  <body>
  <form action='/upload' method='post' enctype='multipart/form-data'>
     <input type='file' name='uploaded_file'>
     <input type='submit' value='Upload'>
  </form>
  '''
if __name__ == '__main__':
  app.run(port=7777)