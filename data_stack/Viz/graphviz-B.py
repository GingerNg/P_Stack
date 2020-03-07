from graphviz import Digraph

"""自动生成一张图并打开"""
g = Digraph('测试图片')
g.node(name='a',color='red')
g.node(name='b',color='blue')
g.edge('a','b',color='green')
g.view()