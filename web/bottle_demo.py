"""
bottle web 框架
"""

from bottle import Bottle, run
app = Bottle()
@app.route('/hello')
def hello():
    return "Hello World!"

run(app, host='localhost', port=8080)



# if __name__ == '__main__':
#     def application(environ, start_response):
#         start_response('200 OK', [('Content-Type', 'text/html')])
#         return ['<h1>Hello world!</h1>']
#
#
#     run(host='localhost', port=8080, app=application)