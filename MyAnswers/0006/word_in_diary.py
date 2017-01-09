# usr/bin/python
# -*- coding: utf-8 -*-

'''
**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''

from collections import Counter
import re
import sys


def get_word(txt):
    common_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this', 's', 'is', 'are', 'a', 'with', 'as', 'an']
    file_text = open(txt, 'r', encoding='UTF-8')
    content = file_text.read().lower()

    pattern = '[a-z0-9\']+'
    word = re.findall(pattern, content)
    word_list = Counter(word)
    for wor in word_list:
        if wor in common_word:
            word_list[wor] = 0
    file_text.close()

    return word_list.most_common()[:3]


d = get_word('/Users/leonhart/Documents/Git/TestTxt/TestTxt.txt')
print(d)
