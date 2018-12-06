# coding = utf-8

from basic.meta_class import CleanerMeta
class APIBase(object):
    __metaclass__ = CleanerMeta   # Integer = IntMeta('Integer', (int, ), {})

    # ...