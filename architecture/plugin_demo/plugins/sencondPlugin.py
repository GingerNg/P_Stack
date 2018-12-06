#coding:utf-8
import sys
sys.path.append('../')

from architecture.plugin_demo import Plugin

__all__ = ["SecondPlugin"]  # 被导入模块若定义了__all__属性，则只有__all__内指定的属性、方法、类可被导入。

class SecondPlugin(Plugin):
   
    name = "secondPlugin"
    version = '0.0.1'

    def __init__(self):
        Plugin.__init__(self)

    def scan(self, config={}):
        return "second plugin"