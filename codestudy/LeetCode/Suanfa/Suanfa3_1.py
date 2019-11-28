'''
背包问题：每件物品可分割为0-1中任意一份：
考虑每次将单位价值最大的物品放入
'''
from typing import List
'''
输入为:things列表其中每个列表元素都是个二元元列表第一个元素为物品价值第二个元素为物品的重量
       w：背包容量 
'''
def get_maxValue(things:List[List],w)->float:
    sorted_things=sorted(things,key=lambda s: (s[0]/s[1]),reverse=True)
    answer=0
    remain=w
    for i in range(len(things)):
        if(remain<=sorted_things[i][1]):
            answer+=sorted_things[i][0]*remain/sorted_things[i][1]
            break
        else:
            answer+=sorted_things[i][0]
            remain=remain-sorted_things[i][1]


    return answer
print(get_maxValue([[50,10],[120,30],[60,20]],50))






