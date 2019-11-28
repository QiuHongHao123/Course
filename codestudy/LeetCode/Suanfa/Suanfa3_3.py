'''
最佳生产方案
'''
from typing import List
'''
输入为两个List第一个存储了各个月的生产花费第二个存储了各个月需求
'''
def get_min_cost(c:List,y:List):
    sumcost=0
    for i in range(len(y)-1,-1,-1):
        bestchoose=y[i]*c[i]
        for k in range(i):
            bestchoose=min(bestchoose,y[i]*((i-k)+c[k]))
        sumcost+=bestchoose
    return sumcost
print(get_min_cost([2,5,3],[2,5,4]))