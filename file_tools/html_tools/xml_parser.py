

from xml.dom.minidom import parse
DOMTree=parse(r'./cases/report123/content.xml')

elelist=DOMTree.documentElement

for ele in elelist:
    print(ele)