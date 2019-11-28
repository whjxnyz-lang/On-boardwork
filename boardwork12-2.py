# -*- coding: utf-8 -*-
# 将文章格式修正
#【问题描述】
# 文件unformatted.txt存储的是一篇英文文章，格式编码上有两个问题
# (1) 句子开头可能是小写字母
# (2) 句子中间可能有大写字母
# 修正格式存入formatted.txt
# 句子只能出现在
# (1)  段落开头，即换行符之后(句子开头可能有空格)
# (2)  西文句号，叹号和分号之后（可能隔有空格）
#【输入形式】
# 从文件输入，文件名为unformatted.txt
#【输出形式】
# 输出为文件，文件名为formatted.txt
#【样例输入】
#   this is A tEst. OK!  
#【样例输出】
# This is a test. Ok! 
import re

# 这里定义一个方法把字符串首字母大写
def normalize(name):
    name = name.lstrip()  # 去掉句子左侧空格
    if name.isspace():  # 如果句子是空格
        return name
    else:
        # return name[0].upper() + name[1:].lower()
        return name.capitalize()

# 定义句子还原
def originsentences(l1):
    return " ".join(str(i) for i in l1)

def formatsentences():
    #读取文件
    ms = open("unformatted.txt")  
    #逐行写入
    for line in ms.readlines():  
        with open("formatted.txt","a") as mon:
            # mon.write(line)  
            sentences = re.split(r"([.!?;])", line)
            sentences.append("")
            sentences = ["".join(i) for i in zip(sentences[0::2], sentences[1::2])]
            print(sentences)
            L1 = list(map(normalize, sentences))
            print(L1)
            # 将句子还原
            # str = " ".join(str(i) for i in L1)
            str = originsentences(L1)
            print(str)
            mon.write(str)
            

if __name__ == '__main__':
    formatsentences()