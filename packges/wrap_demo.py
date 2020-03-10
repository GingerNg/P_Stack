
from textwrap import wrap
para = 'Hello, [world](http://earth.google.com/)! ![](http://n.sinaimg.cn/translate/485/w512h773/20180728/aYof-hfxsxzf8508060.jpg)'
test = 'Hello, [world](http://earth.google.com/)! ![](http://n.sinaimg.cn/translate/485/w512h773/20180728/aYof-'
print(len(para))
print(len(test))
result = ""
# result += "\n".join(
#                         wrap(para, 78)
#                     )
result = wrap(para,78, break_long_words=False)

print(result)