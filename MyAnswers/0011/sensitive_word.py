# !usr/bin/python
# -*- coding: utf-8 -*-

"""
**第 0011 题：** 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

    北京
    程序员
    公务员
    领导
    牛比
    牛逼
    你娘
    你妈
    love
    sex
    jiangge
"""

import re

def sensitive_new_word(path):
    sensitive = []
    #"//Users//leonhart//Documents//Git//ShowMeTheCode//MyAnswers//0011//SensitiveWord.txt"
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            sensitive.append(line.strip())
        print(sensitive)
    return sensitive

def check_sensitive(word_list):
    flag = 0
    text = input()
    # for word in word_list:
    #     if re.search(word,text) is not None:
    #         print("Freedom")
    #         flag = 1
    #         break
    #     else:
    #         pass
    # if flag == 0:
    #     print("Human Rights")
    if any([i in text for i in word_list]):
        print("freedom")
    else:
        print("human")

path = "//Users//leonhart//Documents//Git//ShowMeTheCode//MyAnswers//0011//SensitiveWord.txt"
check_sensitive(sensitive_new_word(path))



