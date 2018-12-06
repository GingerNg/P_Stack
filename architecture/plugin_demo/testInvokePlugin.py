#coding:utf-8
from architecture.plugin_demo.pluginManager import DirectoryPluginManager

if __name__=='__main__':
    plugin_manager = DirectoryPluginManager()
    plugin_manager = DirectoryPluginManager(config={"directories":("C:\XXX\PycharmProjects\plugins",)})
    plugin_manager.loadPlugins()
    plugins = plugin_manager.getPlugins("firstPlugin")
    
    print ("**"*30)
    print (plugins[0].execFun())