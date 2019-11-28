from typing import  List
def get_max(nums:List[int],x)-> bool:
    flag=False
    lenth=len(nums)
    nums=sorted(nums)
    i=0
    j=lenth-1
    while i<j:
        if nums[i]+nums[j]>x:
            j-=1
        elif nums[i]+nums[j]<x:
            i+=1
        else:
            flag=True
            break
    return flag
print(get_max([9,1,2,3,4,5],14))
