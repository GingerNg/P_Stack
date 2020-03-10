# -*- coding: utf-8 -*-
# mark_point.py
# @author Ginger
# @description
# @created 2020-03-09T16:16:03.003Z+08:00
#

from PIL import Image
from pylab import *
import os

full_path = os.getcwd()+"/file_tools/pdf_tools"+'/vec5_filter.png'
im = array(Image.open(full_path))
imshow(im)
print('点击图像当中要拾取的点：')
x = ginput(5)
print('输出坐标位置:', x)
