#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: img_util.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-30 下午5:37
 @desc:

im.rotate(45)

 python图像处理：pytesseract和PIL  (常用函数介绍)
https://www.cnblogs.com/yinzx/p/4741986.html

归一化
http://blog.csdn.net/lenovojxn/article/details/53768537

https://www.cnblogs.com/yushuo1990/p/5879596.html
"""


from PIL import Image
from PIL import ImageEnhance
import numpy as np
import utils.distance_util
import utils.transform_util
import utils.file_util
import matplotlib.pyplot as plt


# 归一化
# http://blog.csdn.net/lenovojxn/article/details/53768537
def max_min_normalization(data_value, data_col_max_values = None, data_col_min_values = None):
    """ Data normalization using max value and min value

    Args:
        data_value: The data to be normalized
        data_col_max_values: The maximum value of data's columns
        data_col_min_values: The minimum value of data's columns
    """
    if data_col_max_values is None:
        data_col_max_values = data_value.max(axis=0)
    if data_col_min_values is None:
        data_col_min_values = data_value.min(axis=0)
    data_shape = data_value.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]
    for i in range(0, data_rows, 1):
        for j in range(0, data_cols, 1):
            max_min = data_col_max_values[j] - data_col_min_values[j]
            if max_min == 0:
                data_value[i][j] = 0
            else:
                data_value[i][j] = \
                    (data_value[i][j] - data_col_min_values[j]) / \
                    max_min
    img = Image.fromarray(data_value)
    img.save('/home/XXX/img.jpg')
    return data_value



mime_list = ['.jpg','.tiff','.png']

img_o = Image.open('PATH/image_code_A.jpg')

print (img_o.format, img_o.size, img_o.mode)
img=np.array(img_o)


box_parm = [0, 0, 30, 30]

def direction_crop(img_o,initial_box,direction = 'right'):
    __right(img_o=img_o,initial_box=initial_box)

def __right(img_o,initial_box):  # transverse
    [x,y] = img_o.size
    step = initial_box[2]-initial_box[0]
    while (initial_box[2]<=x):
        box = tuple(initial_box)
        region = img_o.crop(box)  # 左上角为 (0, 0)的坐标系统  （距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
        initial_box[2] = initial_box[2]+step
        initial_box[0] = initial_box[0]+step
        region.save("PATH/patches_A/"+str(box[0])+'.jpg')
        # plt.figure("crop"+str(box[0]))
        # region.show()
        # img_o.paste(region)

def __down(img_o,initial_box):
    pass

def sliding_window(img_o,save_path = 'PATH/patches_A/',step =10,wh = [30,30]):
    [x, y] = img_o.size
    box_parm = [0,0]+wh
    cnt = 0
    while(box_parm[3]<=y):
        initial_box = list(box_parm)
        while(box_parm[2]<=x):
            box = tuple(box_parm)
            region = img_o.crop(box)  # 左上角为 (0, 0)的坐标系统  （距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
            cnt +=1
            region.save(save_path + str(cnt) + '.jpg')
            box_parm[2] = box_parm[2] + step  # 往右移动
            box_parm[0] = box_parm[0] + step
        box_parm[1]=box_parm[1]+step
        box_parm[3]=box_parm[3]+step   # 往下移动
        box_parm[0]=initial_box[0]
        box_parm[2]=initial_box[2]

'''
按像素值的变化,得到目标patch
'''
def get_target_patches(patches_path ='/home/XX/patches_B/' ,crop_num = 30):
    target_list = []
    crop_list = []
    for file_name in range(crop_num):  # 有序
        img_o = Image.open('/home/XXX/patches_B/'+str(file_name+1)+'.jpg')
        img = np.array(img_o)
        # print file_name,img.max(0),img.min(0),'\n'
        # a.sum(axis=0,1)#axis为0计算全部数据的和，为1则按行计算数据的和
        # print img.sum(0)
        print (file_name, sum(img.min(0)))
        crop_list.append(sum(img.min(0)))
    # start = crop_list[0]
    updown = True  # down True, up False
    for i in range(len(crop_list)-1):
        gradient = crop_list[i+1]-crop_list[i]
        if gradient==0:
            continue
        if gradient<0 and not updown:
            # print i
            updown = not updown
        if gradient>0 and updown:
            print (i)
            target_list.append(i)
            updown = not updown
    return target_list

def preprocess(img_path,save_path = None):
    img_o = Image.open(img_path)
    imgry = img_o.convert('L')  # 图像加强，二值化
    sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    sharp_img = sharpness.enhance(1)
    if save_path is not None:
        sharp_img.save(save_path)
    return sharp_img


if __name__ =='__main__':
    img_o.show()
    # img_n = max_min_normalization(img)
    # direction_crop(img_o,box_parm)
    # sliding_window(img_o)
    img_o = Image.open('/home/XX/image_code_B.jpg')
    imgry = img_o.convert('L')  # 图像加强，二值化
    sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    sharp_img = sharpness.enhance(1)
    sharp_img.save("/home/XX/image_code_sharp.jpg")
    my = Image.open("/home/XXX/image_code_sharp.jpg")
    sliding_window(my, save_path='/home/XX/patches_B/')

    target_list = []
    crop_list = []
    for file_name in range(30):  # 有序
        img_o = Image.open('/home/XX/patches_B/'+str(file_name+1)+'.jpg')
        img = np.array(img_o)
        # print file_name,img.max(0),img.min(0),'\n'
        # a.sum(axis=0,1)#axis为0计算全部数据的和，为1则按行计算数据的和
        # print img.sum(0)
        print (file_name, sum(img.min(0)))
        crop_list.append(sum(img.min(0)))
    # start = crop_list[0]

    updown = True  # down True, up False
    for i in range(len(crop_list)-1):
        gradient = crop_list[i+1]-crop_list[i]
        if gradient==0:
            continue
        if gradient<0 and not updown:
            # print i
            updown = not updown
        if gradient>0 and updown:
            print (i)
            target_list.append(i)
            updown = not updown

    img = preprocess('/home/XX/image_code_A.jpg',"/home/XXX/image_code_A_sharp.jpg")
    # data_col_max_values = np.array(img).max(axis=0)
    # data_col_min_values = np.array(img).min(axis=0)
    sliding_window(img, save_path='/home/XX/patches_A/')

    for target in target_list:
        distance_list = []
        img_b_array = np.array(Image.open('/home/XX/patches_B/' + str(target) + '.jpg'))
        img_b = np.mat(max_min_normalization(img_b_array))
        img_bb = np.mat(utils.transform_util.lists_to_list(img_b.tolist()))
        for file_name in range(240):  # 有序
            img_a_array = np.array(Image.open('/home/XX/patches_A/' + str(file_name + 1) + '.jpg'))
            img_a = max_min_normalization(img_a_array)
            im_aa = np.mat(utils.transform_util.lists_to_list(img_a))
            distance_list.append(utils.distance_util.hamming(img_bb, im_aa))
        print (distance_list.index(min(distance_list)))
        print (distance_list)






        # img转向量



    # 向量计算distance













