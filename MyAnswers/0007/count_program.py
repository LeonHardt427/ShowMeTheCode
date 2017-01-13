# !usr/bin/python
# -*- coding:utf-8 -*-

"""
**第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import re



def program_counter (program_name):
    count_result = {"Program":0, "annotation":0, "blank":0}
    flag = 1
    file_open = open(program_name, 'r', encoding='UTF-8')
    file_lines = file_open.readlines()
    for line in file_lines :
        """
        当处于三个"的注释中时,不断增加annotation
        """
        if flag == 0:
            if re.match("\s*'''", line) is not None or re.match("\s*\"\"\"", line) is not None:
                count_result["annotation"] += 1
                flag = 1
                continue
            else:
                count_result["annotation"] += 1
                continue
        """
        当不处于三个"中时,判断其它的
        """
        if flag == 1:
            if "#" in line and flag == 1:
                if line.startswith("#"):     #re.match("^\s*#", line)
                    count_result["annotation"] += 1
                else:
                    count_result["Program"] += 1
                    count_result["annotation"] += 1
            #匹配三个"的注释开头
            elif re.match("\s*'''", line) is not None or re.match("\s*\"\"\"", line) is not None :
                count_result["annotation"] += 1
                flag = 0
            elif line == "\n":
                count_result["blank"] += 1
            else:
                count_result["Program"] += 1
    print(count_result)
    return count_result

program = "/Users/leonhart/Documents/Git/ShowMeTheCode/MyAnswers/0001/ActivationCode.py"
program_counter(program)












