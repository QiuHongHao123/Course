#使子序列中最大值的和最小
from typing import  List

def minsmax(nums:List[int],B:int)->int:

    lenth=len(nums)
    if lenth==1:
        return nums[0]
    sum=0
    minmax=float('inf')
    for i in range(lenth-1,-1,-1):
        sum=sum+nums[i]
        if sum<=B:
            minmax=min(max(nums[i:])+minsmax(nums[:i],B),minmax)
        else:
            break
    return minmax

print(minsmax([2,2,2,8,1,8,2,1],20))