# coding:utf8
# author:ginger
# http://stackoverflow.com/questions/1036409/recursively-convert-python-object-graph-to-dictionary/22679824#22679824
# convert obj to dict
import collections
try:
  # Python 2.7+
  basestring
except NameError:
  # Python 3.3+
  basestring = str

def todict(obj):
  """ 
  Recursively convert a Python object graph to sequences (lists)
  and mappings (dicts) of primitives (bool, int, float, string, ...)
  """
  if isinstance(obj, basestring):
    return obj
  elif isinstance(obj, dict):
    return dict((key, todict(val)) for key, val in obj.items())
  elif isinstance(obj, collections.Iterable):
    return [todict(val) for val in obj]
  elif hasattr(obj, '__dict__'):
      # var():如果默认不输入参数，就打印当前调用位置的属性和属性值，相当于locals()的功能。
    return todict(vars(obj))  # vars():本函数是实现返回对象object的属性和属性值的字典对象
  elif hasattr(obj, '__slots__'):
    return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
  return obj

class A(object):
    def __init__(self):
        self.b=1
        self.c=2
    def do_nothing(self):
        pass

class B(object):
    def __init__(self):
        a = A()
        self.d = 6
        self.e = 7
    def do_nothing(self):
        pass

b = B()
print (vars(b))
print (b.__dict__)
print (todict(b)) # {'e': 7, 'd': 6}
print (type(todict(b)))
#print type(b)