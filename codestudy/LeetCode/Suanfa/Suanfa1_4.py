from typing import List
def getmMaxSum1(nums:List[int])->int:
    lenth=len(nums)
    if lenth==1:
        return nums[0]

    left=getmMaxSum1(nums[:lenth//2])
    right=getmMaxSum1(nums[lenth//2:])
    lsum=nums[lenth//2-1]
    sum=0
    for i in range(lenth//2-1,-1,-1):
        sum=sum+nums[i]
        if sum>lsum:
            lsum=sum
    rsum=nums[lenth//2]
    sum=0
    for i in nums[lenth//2:]:
        sum=sum+i
        if sum>rsum:
            rsum=sum
    mid=rsum+lsum
    return max(mid,right,left)
def getmMaxSum2(nums:List[int])->int:
    lenth = len(nums)
    sum = 0
    maxsum = nums[0]
    for i in range(0, lenth):
        if sum > 0:
            sum = sum + nums[i]
        else:
            sum = nums[i]
        maxsum = max(maxsum, sum)
    return  maxsum



print(getmMaxSum1([0, -2, 3, 5, -1, 2]))
print(getmMaxSum1([-9, -2, -3, -5, -3]))