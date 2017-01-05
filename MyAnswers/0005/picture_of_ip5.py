#!usr/bin/python
# -*- coding:utf-8 -*-

'''
**第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
'''


import glob                 # 作为通配符自动打开文件
from PIL import Image       # 修改图片属性


'''
  iphone5分辨率为1136x640
'''

def picture_resolution(im):
    print(im.size)
    im.thumbnail((100, 100))
    im.save('thumb.jpg', 'JPEG')


im_picture = Image.open('test.png')
picture_resolution(im_picture)

