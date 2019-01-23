# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: obj_property.py
"""
def prn_obj(obj):
    print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

class A(object):
    def __init__(self,a):
        self.a = a

class B(A):
    def __init__(self, a):
        super().__init__(a)




if __name__ == "__main__":
    a = A(1)

    a.b = 1

    prn_obj(a)