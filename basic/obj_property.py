# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: obj_property.py
"""
def prn_obj(obj):
    print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

class A(object):
    pass

if __name__ == "__main__":
    a = A()

    a.b = 1

    prn_obj(a)