#!usr/bin/python
# -*- coding: utf-8 -*-

''''
**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

import string

word_list = string.ascii_letters

def text_count(text_name):
    count = 0
    for line in text_name.readlines():
        print(line)
        for word in line:
            print(word)
            if word in word_list:
                count += 1
    return count

print(word_list)

with open('test.txt', 'r') as f:
    print(text_count(f))




