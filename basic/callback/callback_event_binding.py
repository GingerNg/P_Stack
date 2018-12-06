#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: callback_event_binding.py
 @author: ginger 
 @software: PyCharm
 @desc: 事件绑定
 http://www.jb51.net/article/68797.htm
"""

class CallbackBase:
    def __init__(self):
        self.__callbackMap = {}
        for k in (getattr(self, x) for x in dir(self)):
            print (k)
            if hasattr(k, "bind_to_event"):
                self.__callbackMap.setdefault(k.bind_to_event, []).append(k)
            elif hasattr(k, "bind_to_event_list"):
                 for j in k.bind_to_event_list:
                    self.__callbackMap.setdefault(j, []).append(k)
  ## staticmethod is only used to create a namespace
    @staticmethod
    def callback(event):
        def f(g, ev = event):    #  g  ===> handler1
            g.bind_to_event = ev
            return g
        return f               #  返回一个函数
    # callback = staticmethod(callback)


    @staticmethod
    def callbacklist(eventlist):
        def f(g, evl = eventlist):
            g.bind_to_event_list = evl
            return g
        return f
    # callbacklist = staticmethod(callbacklist)

    def dispatch(self, event):
        l = self.__callbackMap[event]
        f = lambda *args, **kargs: \
         map(lambda x: x(*args, **kargs), l)
        return f

# ## Sample



class MyClass(CallbackBase):
    EVENT1 = 1
    EVENT2 = 2
    # CallbackBase.callback(EVENT1)
    # CallbackBase.callbacklist([EVENT1, EVENT2])

    @CallbackBase.callback(EVENT1)
    def handler1(self, param = None):
        print ("handler1 with param: %s" % str(param))
        return None

    @CallbackBase.callbacklist([EVENT1, EVENT2])
    def handler2(self, param = None):
        print ("handler2 with param: %s" % str(param))
        return None

    def run(self, event, param = None):
        self.dispatch(event)(param)

if __name__ == "__main__":
    # print (callable(CallbackBase))
    # print (callable(MyClass))
    # # print (callable(MyClass))
    a = MyClass()
    a.run(MyClass.EVENT1,'mandarina')
    # a.run(MyClass.EVENT2,'naranja')