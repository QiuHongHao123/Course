#最大算式
from typing import List
def getMax(nums:List[int],C:int)->int:
    lenth=len(nums)
    dp=[[0]*(C+1) for i in range(lenth)]
    for i in range(lenth):
        for j in range(C+1):
            if j==0:
                dp[i][j]=sum(nums[:i+1])
            else:
                for k in range(j,i+1):
                    dp[i][j] = max(dp[k-1][j-1]*sum(nums[k:i+1]), dp[i][j])


    return dp[lenth-1][C]
print(getMax([1,2,3,4,5],2))