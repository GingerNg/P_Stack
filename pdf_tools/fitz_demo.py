
import os
import fitz 
full_path = os.getcwd()+"/pdf_tools/cases/case55.pdf"
doc = fitz.open(full_path)

for pg in range(doc.pageCount):
    page = doc[pg]  # 获得第pg页
    pm = page.getPixmap(matrix=trans, alpha=False)  # 将其转化为光栅文件（位数）
    # new_full_name = full_path.split(".")[0]  # 保证输出的文件名不变
    # pm.writeImage("%s%s.jpg" % (new_full_name, pg))  # 将其输入为相应的图片格式，可以为位图，也可以为矢量图
    # 我本来想输出为jpg文件，但是在网页中都是png格式（即调用writePNG），再转换成别的图像文件前，最好查一下是否支持