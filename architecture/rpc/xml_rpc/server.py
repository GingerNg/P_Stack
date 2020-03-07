#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
RPC是一个应用层的协议，分为client端和server端，
server端写好了具体的函数实现，client端远程调用该函数，返回函数的结果。
基于的协议: 可以是socket协议,也可以是HTTP协议

http based rpc:
rpc over http（基于http的rpc）有两种协议
一种是xml-rpc --> SOAP
还有一个是 json-rpc

thrift 可跨语言
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
server.register_function(pow)

# Register a function under a different name


def adder_function(x, y):
    return x + y


server.register_function(adder_function, 'add')

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').


class MyFuncs:
    def div(self, x, y):
        return x // y


server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()
