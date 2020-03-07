html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# print(len(html_doc))
# new_html_doc = []
# start = 0
# curs = []
# for i in range(len(html_doc)):
#     if html_doc[i] == ">":
#         start = 1
#     if start:
#         curs.append(html_doc[i])
#     if html_doc[i] == "<":

# html_lines = open("./case3.html","r").readlines()
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("".join(html_doc),'lxml')

# head_tag = soup.head
# # 返回所有子节点的列表
# print(head_tag.contents)
#
# # 返回所有子节点的迭代器
# for child in head_tag.children:
#     print(child)
# for string in soup.strings:
#     print(repr(string))