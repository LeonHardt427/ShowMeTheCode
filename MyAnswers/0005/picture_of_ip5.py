#!usr/bin/python
# -*- coding:utf-8 -*-

'''
**第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
'''


import glob                 # 作为通配符自动打开文件
from PIL import Image       # 修改图片属性
import os


'''
  iphone5分辨率为1136x640
'''

def picture_resolution(im, picture_name):
    print(im.size)
    im.thumbnail((1136, 640))
    im.save(picture_name+'thumb.jpg', 'JPEG')

def pic_basename(pic_full_name):           # 命名中使用原来的名字
    return pic_full_name.split(".")[0]


path = "/Users/leonhart/Documents/Git/TestPicture"
picture_path = glob.glob(path + '/*.jpg')
print(picture_path)

for pic in picture_path:
    pic_name = os.path.basename(pic)
    im_picture = Image.open(pic)
    picture_resolution(im_picture, pic_name)

