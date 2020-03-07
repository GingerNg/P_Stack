
"""
pip3 install pypandoc
pandoc -f docx -t markdown_strict case1.docx -o case2.md
"""
import pypandoc
# pypandoc.convert("./gitword/case1.docx", 'markdown_strict', format='docx',outputfile='case3.md')

import os
import requests
orginal_path = "./orginal"
text_path = "./contract_mds"
for parent, dirnames, filenames in os.walk(orginal_path,  followlinks=True):
    for filename in filenames:
        file_path = os.path.join(parent, filename)
#         print('文件名：%s' % filename)
        print('文件完整路径：%s\n' % file_path)
        pypandoc.convert(file_path, 'markdown_strict', format='docx', outputfile=file_path+'.md')