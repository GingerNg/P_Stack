#coding:utf-8
import sys
sys.path.append('../')

from architecture.plugin_demo import Plugin

__all__ = ["FirstPlugin"]

class FirstPlugin(Plugin):
   
    name = "firstPlugin"
    version = '0.0.1'

    def __init__(self):
        Plugin.__init__(self)

    def scan(self, config={}):
        return "second plugin"
    
    def execFun(self):
        return "second plugin"