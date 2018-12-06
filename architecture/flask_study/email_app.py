#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: email_app.py
 @author: ginger 
 @software: PyCharm
 @desc: 
"""
from flask import Flask, jsonify, abort, make_response, request, url_for
import flask
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

auth = HTTPBasicAuth() # 安全认证

@app.route('/')
def index():
    return "Hello, World!"

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# restful    GET     curl -i http://localhost:5000/todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
# @auth.login_required
def get_tasks():
    return jsonify({'tasks':  map(make_public_task, tasks)})    # 返回json

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)  # 调用not_found函数
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# restful POST (创建资源) curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


# restful PUT (更新资源)   $ curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# restful DELETE (删除资源)
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


# Restful Web Service 安全认证

@auth.get_password
def get_password(username):   # 回调函数
    if username == 'ok':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


# http 500内部服务器（HTTP-Internal Server Error）
# restful POST (创建资源) curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
@app.route('/mail_task', methods=['POST'])
def create_mail_task():
    if not request.json:
        abort(400)  # HTTP 400 错误 - 请求无效 (Bad request);
    # Email.send()
    1/0    #  <Response [500]>
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': 'success'}), 201

# https://www.programcreek.com/python/example/51528/flask.request.files
# http://docs.jinkan.org/docs/flask/patterns/fileuploads.html
@app.route('/mail_result_task', methods=['POST'])
def create_mail_result_task():
    f = flask.request.files['file']
    print (f.stream.read())
    # print f.content_type
    task = {
        'id': tasks[-1]['id'] + 1,
        # 'title': request.json['title'],
        'description': f.stream.read(),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': 'success'}), 201




if __name__ == '__main__':
    app.run(debug=True)