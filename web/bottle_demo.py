"""
https://www.jianshu.com/p/172702c3ac7f
"""
from bottle import get, run


@get("/")
def hello():
    return "hello"


run(host="0.0.0.0", port=8080)

"""使用 tornado来进行部署"""
# run(host="0.0.0.0", port=8080,server="tornado")