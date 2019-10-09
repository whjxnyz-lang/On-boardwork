# -*- coding: utf-8 -*-
# 计算n个a相减
# 输入两个整数a和n
# 整数a大于等于1且小于等于9
# 整数n大于等于1且小于等于80
# +----------------------------------------------+
#  aaa...a  -  aaa...a  -  aaa...a   -  aa  -  a
#    n个a       n-1个a       n-2个a
# +----------------------------------------------+
# 例如输入整数a=5,n=6
# 计算公式 555555-55555-5555-555-55-5
# 样例输入
#  5 6
# 样例输出
# 493830

from functools import reduce
print('请输入整数a和n,两者以空格分隔')
a,n = map(int,input().split())
if not 9>=a>=1:
    print (
        '整数a应大于等于1且小于等于9'
    )
if not 80>=n>=1:
    print(
        '整数n应大于等于1且小于等于80'
    )
Tn = 0
Sn = []
for count in range(n):
    Tn = Tn+a
    a=a*10
    Sn.append(Tn)
    # print (Tn)
print (Sn)
# 将Sn反转
Sn = sorted(Sn,reverse=True)  
print (Sn)
Sn = reduce(lambda x,y: x-y,Sn)
print ("计算为：",Sn)