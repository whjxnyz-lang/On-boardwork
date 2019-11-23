# -*- coding: utf-8 -*-
#文件内的整数排序
#【问题描述】
# 从已知文本文件in.txt中读取存放有若干整数,请将其按照从小到大的顺序排列后存入另一文件out.dat
#【输入形式】
# 文件输入的第一行表示读入数据的个数n;文件输入的第2至n+1行表示各整型数值;
#【输出形式】
# 文件输出的每一行表示个数据值,若输入格式不合法(指n或后续的整数为小数),则输出 illegal input
#【样例输入】
# 从in.txt输入:
# 5
# 
# 3
#
# 92
#
# 15
#
# -3
#
# 0
#【样例输出】
#
# 向 out.dat输出
# -3
#
# 0
# 
# 3
#
# 15
#
# 92

# 这里定义一个排序方法
def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 将in.txt文件读取到arry
file = open("in.txt")
array = []
count = 0
for line in file:
    if line != '\n':
            array.append(int(line))
file.close()
# 对第2到n+1行排序，去除第一行读到的数
array.pop(0)
bubbleSort(array)
print('排序后的输出')
file_name = 'out.dat'
# 将输出写入out.dat
with open(file_name, 'w') as file_obj:
    #先清空文件
    file_obj.truncate()
    for i in range(len(array)):
        print("%d" % array[i])
        file_obj.writelines(str(array[i])+'\n')
