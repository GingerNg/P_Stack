# coding:utf8
# author:ginger

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log('ginger')
def now():
    print '2013-12-25'

def logger(fn):
    def wrapper(*args,**kwargs):
        if type(args[0]) != type(args[1]):
            print("类型不一致请重试")
            return
        z = fn(*args, **kwargs)
        f = open('C:\\Users\\Public\\Documents\\test.txt', 'w')
        f.write(str(z))
        f.close()
        print("finish")
    return wrapper

@logger # add1 = logger(add1)
def add(x,y):
    ret = x + y
    return ret



if __name__ == "__main__":
    now()
    add(12, 56)