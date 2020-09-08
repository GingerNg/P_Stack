import collections


class Student:
    name = ''
    age = 0

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def to_json(self):
        return class_to_dict(self)


stu = Student('', 20)

# 返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()
print(vars(stu))

print(stu.__dict__)


try:
    # Python 2.7+
    basestring
except NameError:
    # Python 3.3+
    basestring = str


def objtodict(obj):
    """
    Recursively convert a Python object graph to sequences (lists)
    and mappings (dicts) of primitives (bool, int, float, string, ...)
    """
    if isinstance(obj, basestring):
        return obj
    elif isinstance(obj, dict):
        return dict((key, objtodict(val)) for key, val in obj.items())
    elif isinstance(obj, collections.Iterable):
        return [todict(val) for val in obj]
    elif hasattr(obj, '__dict__'):
        # var():如果默认不输入参数，就打印当前调用位置的属性和属性值，相当于locals()的功能。
        return objtodict(vars(obj))  # vars():本函数是实现返回对象object的属性和属性值的字典对象
    elif hasattr(obj, '__slots__'):
        return objtodict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
    return obj


print(objtodict(stu))


def class_to_dict(obj):
    '''把对象(支持单个对象、list、set)转换成字典'''
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__
    if is_list or is_set:
        obj_arr = []
        for o in obj:
            # 把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict


print(class_to_dict([stu, stu]))


def convert_to_dict_list(objs):
    '''把对象列表转换为字典列表'''
    obj_arr = []
    for o in objs:
        # 把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
    return obj_arr


convert_to_dict_list([stu, stu])
