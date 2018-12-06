# coding:utf8
# author:ginger
# filenmae: addspam

def addspam(fn):  # addspam is a decorator
    def new(*args):
        print "spam,spam,spam"
        return fn(*args)
    return new

@addspam
def useful(a,b):
    print a**2+b**2

if __name__=="__main__":
    print useful(2,3)