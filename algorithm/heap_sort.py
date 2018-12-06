# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: heap_sort.py
"""
# -*- coding:utf-8 -*-
# 堆排序适用于记录数很多的情况

from collections import deque

# 这里需要说明元素的存储必须要从1开始
# 涉及到左右节点的定位，和堆排序开始调整节点的定位
# 在下标0处插入0，它不参与排序
L = deque([49, 38, 65, 97, 76, 13, 27, 49])  # 两端都可以操作的序列
L.appendleft(0)


# L = [0,49,38,65,97,76,13,27,49]


def element_exchange(numbers, low, high):
    temp = numbers[low]

    # j 是low的左孩子节点(cheer!)
    i = low
    j = 2 * i

    while j <= high:
        # 如果右节点较大，则把j指向右节点
        if j < high and numbers[j] < numbers[j + 1]:
            j = j + 1
        if temp < numbers[j]:
            # 将numbers[j]调整到双亲节点的位置上
            numbers[i] = numbers[j]
            i = j
            j = 2 * i
        else:
            break
    # 被调整节点放入最终位置
    numbers[i] = temp


def top_heap_sort(numbers):
    length = len(numbers) - 1

    # 指定第一个进行调整的元素的下标
    # 它即该无序序列完全二叉树的第一个非叶子节点
    # 它之前的元素均要进行调整
    # cheer up！
    first_exchange_element = int(length / 2)

    # 建立初始堆
    print(first_exchange_element)
    for x in range(first_exchange_element):
        element_exchange(numbers, first_exchange_element - x, length)

    # 将根节点放到最终位置，剩余无序序列继续堆排序
    # length-1 次循环完成堆排序
    for y in range(length - 1):
        temp = numbers[1]
        numbers[1] = numbers[length - y]
        numbers[length - y] = temp
        element_exchange(numbers, 1, length - y - 1)


class Node(object):
    def __init__(self, id, value):
        self.value = value
        self.id = id


# nodes = deque([Node(id=1, value=38),
#                Node(id=2, value=4),
#                Node(id=3, value=25),
#                Node(id=4, value=45)])
#
# nodes.appendleft(Node(id=0, value=32))

def node_exchange(numbers, low, high):
    temp = numbers[low]

    # j 是low的左孩子节点(cheer!)
    i = low
    j = 2 * i

    while j <= high:
        # 如果右节点较大，则把j指向右节点
        if j < high and numbers[j].value < numbers[j + 1].value:
            j = j + 1
        if temp.value < numbers[j].value:
            # 将numbers[j]调整到双亲节点的位置上
            numbers[i].value = numbers[j].value
            i = j
            j = 2 * i
        else:
            break
    # 被调整节点放入最终位置
    numbers[i] = temp


def node_top_heap_sort(nodes):
    length = len(nodes) - 1

    # 指定第一个进行调整的元素的下标
    # 它即该无序序列完全二叉树的第一个非叶子节点
    # 它之前的元素均要进行调整
    # cheer up！
    first_exchange_element = int(length / 2)

    # 建立初始堆
    print(first_exchange_element)
    for x in range(first_exchange_element):
        node_exchange(nodes, first_exchange_element - x, length)

    # 将根节点放到最终位置，剩余无序序列继续堆排序
    # length-1 次循环完成堆排序
    for y in range(length - 1):
        temp = nodes[1]
        nodes[1] = nodes[length - y]
        nodes[length - y] = temp
        node_exchange(nodes, 1, length - y - 1)


if __name__ == '__main__':
    # top_heap_sort(L)
    # for x in range(1, len(L)):
    #     print(L[x])
    # print(L)


    node1 = Node(id=1, value=38)
    node2 = Node(id=2, value=4)
    node3 = Node(id=3, value=25)
    node4 = Node(id=4, value=45)

    updates = {"1":Node(id="1", value=38)}

    nodes = deque([node1,
                   node2,
                   node3,
                   node4])

    node_top_heap_sort(nodes)
    for node in nodes:
        print(node.value)


