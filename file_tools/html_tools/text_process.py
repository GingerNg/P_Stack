

import html2text
h = html2text.HTML2Text()

html_content = open("./gitword/case1.html").read()

fout = open("./gitword/case1.md","w")
# print(html2text.html2text(html_content))
fout.write(html2text.html2text(html_content))