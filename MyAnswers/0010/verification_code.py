# !usr/bin/python
# -*- coding: utf8 -*-


"""
**第 0010 题：**使用 Python 生成类似于下图中的**字母验证码图片**

![字母验证码](http://i.imgur.com/aVhbegV.jpg)

- [阅读资料](http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python)
"""
import random
from PIL import Image, ImageDraw, ImageFont , ImageFilter
import string

code_whole_word = string.ascii_letters + string.digits
weight = 60 * 4
height = 60


def create_code():

    code_key = []
    for num in range(4):
        code_word = random.choice(code_whole_word)
        code_key.append(code_word)

    return code_key


def random_color():
    return (random.randint(64, 225), random.randint(64, 225), random.randint(64, 225))


def random_word_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

image = Image.new('RGB', (weight, height), (255, 255, 255))

font = ImageFont.truetype('Arial.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(weight):
    for y in range(height):
        draw.point((x,y), random_color())

code = create_code()
print(code)

for word in range(4):
    draw.text((60 * word + 10, 10), code[word], font=font, fill=random_word_color())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')



