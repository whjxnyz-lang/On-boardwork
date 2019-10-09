# -*- coding: utf-8 -*-
# 统计最高最低分数和不及格人数
# 从键盘一行输入5个0-100(包含0和100)的整数
# 每个数之间用空格间隔开
# 输出分3行,第一行最高分第二行最低分第三行不及格(低于60不包括60分)的人数
# 样例输入 43 98 78 90 89
# 样例输出
# 98
# 43
# 1

count = 0
passG = 60
print('输入5个0-100(包含0和100)的整数,以空格分隔')
val1,val2,val3,val4,val5 = map(int,input().split())

if val1 < passG:
    count = count + 1

if val2 < passG:
    count = count + 1

if val3 < passG:
    count = count + 1

if val4 < passG:
    count = count + 1

if val5 < passG:
    count = count + 1

print('输出结果')
print('最高分 %d'  %max(val1, val2, val3, val4, val5))
print('最低分 %d'  %min(val1, val2, val3, val4, val5))
print('不及格人数 %d' %count)