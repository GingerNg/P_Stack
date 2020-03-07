#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: __init__.py.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-4 下午11:43
 @desc:
 Spring-cloud : http://m.blog.csdn.net/tanga842428/article/details/73822905

 Raft一致性算法
 分布式系统中的节点通信存在两种模型：共享内存（Shared memory）和消息传递（Messages passing）。
 基于消息传递通信模型的分布式系统，不可避免地会发生以下错误：进程可能会慢、垮、重启，消息可能会延迟、丢失、重复（不考虑“Byzantinefailure”）。
 http://blog.csdn.net/cszhouwei/article/details/38374603


 Consul -- golang  -- Raft算法
 http://tonybai.com/2015/07/06/implement-distributed-services-registery-and-discovery-by-consul/

 etcd A highly-available key value store for shared configuration and service discovery.
 分布式系统中的数据分为控制数据和应用数据
 http://www.infoq.com/cn/articles/etcd-interpretation-application-scenario-implement-principle

服务发现


three layers: up to down
Software-as a Service
Platform-as-a-Service  --- 中间件
IaaS


 熔断机制
"""