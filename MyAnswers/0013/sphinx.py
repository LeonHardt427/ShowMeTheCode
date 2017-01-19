# usr/bin/python
# -*- coding:utf-8 -*-

"""
**第 0013 题：** 用 Python 写一个爬图片的程序，爬 [这个链接里的日本妹子图片 :-)](http://tieba.baidu.com/p/2166231880)

- [参考代码](http://www.v2ex.com/t/61686 "参考代码")
"""

import urllib.request
import re


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def get_image(html):
    reg = r'src="(.*?\.jpg)" bdwater='
    image = re.compile(reg)
    html = html.decode("UTF-8")
    imglist = re.findall(image, html)
    i = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % i)
        i += 1
    return imglist


html = get_html('http://tieba.baidu.com/p/2166231880')
print(get_image(html))
