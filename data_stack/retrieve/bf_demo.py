#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
http://python.jobbole.com/88921/
在搜索过程中使用布隆过滤器可以使得很多没有命中的搜索提前返回来提高效率。
"""
from pybloom import BloomFilter
bf = Bloomfilter(10)
bf.add_value('dog')
bf.add_value('fish')
bf.add_value('cat')
bf.print_contents()
bf.add_value('bird')
bf.print_contents()
# Note: contents are unchanged after adding bird - it collides
for term in ['dog', 'fish', 'cat', 'bird', 'duck', 'emu']:
    print ('{}: {} {}'.format(term, bf.hash_value(term), bf.might_contain(term)))