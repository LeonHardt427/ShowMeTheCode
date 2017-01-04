#coding=utf-8
import random
import string

def gene_activation_code(number,length):
    '''
    @number:生成激活码的个数
    @length:生成激活码的长度
    '''
    result = {}
    source = list(string.ascii_uppercase)
    for index in range(0,10):
        source.append(str(index))
    while len(result) < number:
        key= ''
        for index in range(length):
            key += random.choice(source)
        if key in result:
            pass
        else:
            result[key] = 1
    for key in result:
        print(key)
    print(result)

if __name__ == "__main__":
    number = 10
    length = 16
    gene_activation_code(number,length)
