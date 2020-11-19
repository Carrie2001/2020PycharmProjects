# 导入扩展库
import re  # 正则表达式库
import collections  # 词频统计库
import numpy as np  # numpy数据处理库
import jieba  # 结巴分词
import wordcloud  # 词云展示库
from PIL import Image  # 图像处理库
import matplotlib.pyplot as plt  # 图像展示库


def zhuanhua(x):
    asc = ord(x)
    num = asc - 96
    return num


def jisuan(x):
    list_zimu = list(x)
    sum = 0

    for i in list_zimu:
        if zhuanhua(i) < 0 and zhuanhua(i) > 26:
            break
        else:
            sum = zhuanhua(i) + sum
    return sum


# 读取文件
fn = open('30000.txt')  # 打开文件
string_data = fn.read()  # 读出整个文件
fn.close()  # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data)  # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all=False)  # 精确模式分词
object_list = []

for word in seg_list_exact:  # 循环读出每个分词
    object_list.append(word)  # 分词追加到列表

outputFile = open('result.txt', 'w')

for j in object_list:
    print(j, jisuan(j))
    if jisuan(j) == 100:
        outputFile.writelines(i + '\n')