#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: event_listen.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-21 下午11:12
 @desc: 
"""

class Event(object):
    """
    Generic event to use with EventDispatcher.
    用于事件分发
    """

    def __init__(self, event_type, data=None):
        """
        The constructor accepts an event type as string and a custom data
        定义event的类型和数据
        """
        self._type = event_type
        self._data = data

    @property
    def type(self):
        """
        Returns the event type
        返回event类型
        """
        return self._type

    @property   # A decorator
    def data(self):
        """
        Returns the data associated to the event
        返回event传递的数据
        """
        return self._data


class EventDispatcher( object ):   # 事件分发器
    """
    Generic event dispatcher which listen and dispatch events
    event分发类 监听和分发event事件
    """

    def __init__(self):
        """
        初始化类
        """
        self._events = dict()  # 持有一个事件字典

    def __del__(self):
        """
        清空所有event
        """
        self._events = None

    def has_listener(self, event_type, listener):
        """
        Return true if listener is register to event_type
        返回注册到event_type的listener
        """
        # Check for event type and for the listener
        if event_type in self._events.keys():
            return listener in self._events[ event_type ]
        else:
            return False

    def dispatch_event(self, event):
        """
        Dispatch an instance of Event class
        """
        # 分发event到所有关联的listener
        if event.type in self._events.keys():
            listeners = self._events[ event.type ]

            for listener in listeners:
                listener( event )

    def add_event_listener(self, event_type, listener):   # listener是一个回调函数
        """
        Add an event listener for an event type
        给某种事件类型添加listener
        """
        # Add listener to the event type
        if not self.has_listener( event_type, listener ):
            listeners = self._events.get( event_type, [] )

            listeners.append( listener )

            self._events[ event_type ] = listeners

    def remove_event_listener(self, event_type, listener):
        """
        移出某种事件类型的所以listener
        """
        # Remove the listener from the event type
        if self.has_listener( event_type, listener ):
            listeners = self._events[ event_type ]

            if len( listeners ) == 1:
                # Only this listener remains so remove the key
                del self._events[ event_type ]

            else:
                # Update listeners chain
                listeners.remove( listener )

                self._events[ event_type ] = listeners

class MyEvent( Event ):
    """
    When subclassing Event class the only thing you must do is to define
    a list of class level constants which defines the event types and the
    string associated to them
    """

    ASK = "askMyEvent"
    RESPOND = "respondMyEvent"
# The method is very simple, only two events are implemented, ASK and RESPOND.

class WhoAsk(object):    # 监听 respondMyEvent事件
    """
    First class which ask who is listening to it
    """
    def __init__(self, event_dispatcher):
        # Save a reference to the event dispatch
        self.event_dispatcher = event_dispatcher

        # Listen for the RESPOND event type
        self.event_dispatcher.add_event_listener(
            MyEvent.RESPOND, self.on_answer_event
        )

    def ask(self):   # 发生ask事件
        """
        Dispatch the ask event
        """
        print ">>> I'm instance {0}. Who are listening to me ?".format( self )

        self.event_dispatcher.dispatch_event(
            MyEvent( MyEvent.ASK, self )   # 分发器分发,找到相应的listener,并执行(回调)
        )

    def on_answer_event(self, event):
        """
        Event handler for the RESPOND event type
        """
        print "<<< Thank you instance {0}".format( event.data )

class WhoRespond( object ):
    """
    Second class who respond to ASK events
    """
    def __init__(self, event_dispatcher):
        # Save event dispatcher reference
        self.event_dispatcher = event_dispatcher

        # Listen for ASK event type
        self.event_dispatcher.add_event_listener(   # 监听askMyEvent事件
            MyEvent.ASK, self.on_ask_event
        )

    def on_ask_event(self, event):    # 监听ask事件
        """
        Event handler for ASK event type
        """
        self.event_dispatcher.dispatch_event(
            MyEvent ( MyEvent.RESPOND, self )
        )

if __name__ == '__main__':
    event_dispatcher = EventDispatcher()
    whoAsk = WhoAsk(event_dispatcher)
    whoRespond = WhoRespond(event_dispatcher)
    whoAsk.ask()