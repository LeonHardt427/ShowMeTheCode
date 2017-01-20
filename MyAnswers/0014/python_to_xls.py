#!usr/bin/env python
# -*-coding:utf-8 -*-

"""
**第 0014 题：** 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

    {
    	"1":["张三",150,120,100],
    	"2":["李四",90,99,95],
    	"3":["王五",60,66,68]
    }

"""

import os
import json
import xlwt

student_path = "/Users/leonhart/Documents/Git/TestTxt/"


def python_to_xls(path):
    os.chdir(path)
    with open('TestXls.txt', encoding='UTF-8') as f:
        content = f.read()

    content_json = json.loads(content)

    sheet = xlwt.Workbook()
    table = sheet.add_sheet('city')
    for row, i in enumerate(list(content_json)):
        table.write(row, 0, i)
        for coj, j in enumerate(content_json[i]):
            table.write(row, coj + 1, j)

    sheet.save('student.xls')


if __name__ == "__main__":
    python_to_xls(student_path)
