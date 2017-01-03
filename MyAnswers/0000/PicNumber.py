#!usr/bin/python
#-*-coding: utf-8 -*-


##第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont

im = Image.open('Test.jpg')
print(im.format,im.size, im.mode)

draw = ImageDraw.Draw(im)
##draw.text((0,0), "4", fill = (255,0,0))

text = "4"
Font1 = ImageFont.truetype("SFCompactText-Bold.otf" , 20)


draw.text([112,0],text ,font = Font1)





im.show()







