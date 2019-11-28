from typing import List
def get_shiftnum(nums:List[int]):
    lenth=len(nums)
    if lenth==1:
        return 0
    i=0
    for i in range(0,lenth-1):
        if nums[i]>nums[i+1]:
            return i+1
print(get_shiftnum([4,1,2,3]))