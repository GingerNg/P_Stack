#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: feature_util.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-12-1 下午1:31
 @desc:
 sift:
 http://blog.csdn.net/handsomekang/article/details/41448697
"""

# coding=utf-8
import cv2
import scipy as sp

img1 = cv2.imread('x1.jpg', 0)  # queryImage
img2 = cv2.imread('x2.jpg', 0)  # trainImage

# Initiate SIFT detector
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

if __name__ == '__main__':
    img = cv2.imread("PATH/image_code_B_2.jpg")
        # 创建窗口并显示图像
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
        # 释放窗口
    cv2.destroyAllWindows()