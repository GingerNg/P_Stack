# coding:utf8
# author:ginger
import logging

#  ?
logging.basicConfig(level = logging.INFO)

def checkParams(fn):
    def wrapper(a,b):
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return fn(a,b)

        logging.warning("variable 'a' and 'b' can't be added")
        return
    return wrapper


@checkParams
def add(a,b):
    return a+b




if __name__ =="__main__":
    print add(3,8)
  #  add = checkParams(add)  使用语法糖可以代替这一句！！！
    print type(add)
    print add(3,8)

    add(3,'hello')