#!usr/bin/python
# -*-coding:utf-8 -*-


# 第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券)
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
import string

source_code = string.ascii_uppercase + string.digits   #邀请码为26个英文大写字母和0-9十个数字随机组合而成
def activation_code(number = 10 , length = 10):
    code_list = {}
    code = ""
    for count in range(number):
        key_name = "key"+ str(count)
        for num in range(length):
            code = code + random.choice(source_code)
        code_list[key_name] = code
        code = ""
    return code_list

c = activation_code()
for key in c :
    print("C[%s]="% key, c[key])

print(c)