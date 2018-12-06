#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
topological sort
Kahn
基于DFS的拓扑排序
"""

class GraphNode(object):
    def __init__(self,name=""):
        self.__pre = []
        self.__back = []
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def getIndegree(self):
        return len(self.__pre)

    def setPre(self,pre):
        self.__pre.append(pre)

    def setBack(self,back):
        self.__back.append(back)

    def getPre(self):
        return self.__pre

    def getBack(self):
        return self.__back



def kahn_topological(graphNodes):
    """
    L← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edges
    :return: L list
    """
    L = []
    S = []
    S =getZeroIncomingDegreeNode(graphNodes,S)
    while len(S)>0:
        zeroNode = S.pop()
        L.append(zeroNode)
        S = getZeroIncomingDegreeNode(graphNodes,S,zeroNode=zeroNode)
    return L

def getZeroIncomingDegreeNode(graphNodes,S,zeroNode = None):
    toBeRemoved = []
    for graphNode in graphNodes:
        try:
            graphNode.getPre().remove(zeroNode)
        except ValueError:
            print ("---")
        if graphNode.getIndegree() == 0:  # 当入度==0 则加入结果集
            S.append(graphNode)
            toBeRemoved.append(graphNode)
    for removed in toBeRemoved:
        graphNodes.remove(removed)
    return S



def dfs_topological():
    """

    :return:
    """
    pass

if __name__ == "__main__":
    nodeA = GraphNode("a")
    nodeB = GraphNode("b")
    nodeC = GraphNode("c")
    nodeD = GraphNode("d")
    nodeE = GraphNode("e")
    nodeF = GraphNode("f")

    # nodeA.setBack([nodeB,nodeD])
    nodeB.setPre(pre=nodeA)
    # nodeB.setBack(nodeC)
    nodeC.setPre(pre=nodeB)
    # nodeC.setBack([nodeE,nodeD])
    nodeD.setPre(pre=nodeA)
    nodeD.setPre(nodeC)
    # nodeD.setBack(nodeE)
    nodeE.setPre(pre=nodeC)
    nodeE.setPre(nodeD)

    graphNodeList = [nodeA,nodeB,nodeC,nodeD,nodeE,nodeF]
    print (nodeA.getIndegree())

    results =  kahn_topological(graphNodeList)
    for result in results:
        print (result.getName())

    # testList = [1,2,3]
    # # print testList.pop()
    # test = testList[0]
    # testList.remove(1)
    # print testList
    # print test
    # test1 = []
    # test1.append(testList.pop())
    # print test1
    # print testList