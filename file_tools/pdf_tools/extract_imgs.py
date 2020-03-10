
import sys
from PIL import Image
import numpy as np
from pylab import *
import os
import fitz
import cairosvg
sys.setrecursionlimit(150000)

work_path = os.getcwd()+"/file_tools/pdf_tools/pdfs/"

file_name = "电力行业：区域整合，火电自救的又一破局点－热点专题系列（四）-光大证券191201.pdf"
# file_name = "餐饮旅游行业：经济数据边际企稳，优质龙头和低估值航空股迎布局良机－周报20191202-民生证券191202.pdf"
full_path = work_path + file_name
doc = fitz.open(full_path)
page = doc[1]
svg = page.getSVGimage(matrix=fitz.IdentityMatrix)
open(work_path+"vec6.svg", "w").write(svg)

cairosvg.svg2png(url=work_path+'vec6.svg', write_to=work_path+'vec6.png')

image = Image.open(work_path+"vec6.png")
buffer = []
for pixel in image.getdata():
    buffer.append((
        pixel[0],
        pixel[1],
        pixel[2],
        # pixel[3]-150,
    ))
image.putdata(buffer)

image.save(work_path+'vec6_filter.png')

image = Image.open(work_path + "vec6_filter.png")
# for pixel in image.getdata():
#     print(pixel)
im = np.array(image)


def is_black(pixel):
    if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
        return True


def walk(point, regions_x, regions_y, dire="11111111", Points=[]):
    if point in Points:
        return
    if point[0] >= 0 and point[0] < im.shape[0] and point[1] >= 0 and point[1] < im.shape[1]:
        pixel = im[point[0], point[1]]
        if not is_black(pixel):
            regions_x.append(point[0])
            regions_y.append(point[1])
            # regions.append(point)
            if dire[0] == "1":
                walk([point[0]+1, point[1]], regions_x,
                     regions_y, dire="10000000", Points=Points)
            if dire[1] == "1":
                walk([point[0]+1, point[1]+1], regions_x,
                     regions_y, dire="01000000", Points=Points)
            if dire[2] == "1":
                walk([point[0], point[1]+1], regions_x,
                     regions_y, dire="00100000", Points=Points)
            if dire[3] == "1":
                walk([point[0]-1, point[1]+1], regions_x,
                     regions_y, dire="00010000", Points=Points)
            if dire[4] == "1":
                walk([point[0]-1, point[1]], regions_x,
                     regions_y, dire="00001000", Points=Points)
            if dire[5] == "1":
                walk([point[0]-1, point[1]-1], regions_x,
                     regions_y, dire="00000100", Points=Points)
            if dire[6] == "1":
                walk([point[0], point[1]-1], regions_x,
                     regions_y, dire="00000010", Points=Points)
            if dire[7] == "1":
                walk([point[0]+1, point[1]-1], regions_x,
                     regions_y, dire="00000001", Points=Points)


def rect_grow(point, rects):
    global regions_x
    global regions_y
    global Points
    Points = []
    regions_x = []
    regions_y = []
    walk(point, regions_x=regions_x, regions_y=regions_y, Points=Points)
    if len(regions_x) > 0 and len(regions_y) > 0:
        min_x = min(regions_x)
        max_x = max(regions_x)
        min_y = min(regions_y)
        max_y = max(regions_y)
        if max_x - min_x > 50 and max_y - min_y > 50:
            rects.append([min_x, max_x, min_y, max_y])
    # return rects


def is_in_rects(point, rects):
    for rect in rects:
        if point[0] >= rect[0] and point[0] <= rect[1] and point[1] >= rect[2] and point[1] <= rect[3]:
            return True


def search_rect():
    """
    在page页面搜索非背景部分，形成矩形框
    """
    rects = []
    for y in range(0, im.shape[1]):
        for x in range(0, im.shape[0]):
            pixel = im[x, y]
            point = [x, y]
            if not is_black(pixel) and not is_in_rects(point, rects):
                # return pixel,point
                rect_grow(point, rects)
            # if len(rects)>0:
            #     return rects
    return rects


rects = search_rect()
print(rects)


def crop(rect, im, i):
    crop_im = im[rect[0]:rect[1], rect[2]:rect[3]]
    crop_im = Image.fromarray(crop_im)
    crop_im.save(work_path + "imgs/res_%s.png" % i)


for i in range(len(rects)):
    crop(rects[i], im, i)
