# coding:utf8
# author:ginger
# filenmae: addspam
import time


def addspam(fn):  # addspam is a decorator
    def new(*args):
        print ("before")
        fn(*args)
        print("after")
    return new

def statistic(fn):
    def new(*args):
        start = time.time()
        fn(*args)
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (fn.__name__, (end - start)))
    return new

@addspam
def useful(a,b):
    print (a**2+b**2)

@statistic
def useful_s(a,b):
    print (a**2+b**2)

if __name__=="__main__":
    useful(2,3)
    useful_s(2, 3)

