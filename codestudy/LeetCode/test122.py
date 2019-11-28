from typing import  List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #动态规划股票问题不懂看收藏
        if not prices:
            return 0
        day=len(prices)

        for i in range(day):
            if i==0:
                bp_i_0=0
                bp_i_1=-prices[0]
                continue
            tmp = bp_i_0
            bp_i_0=max(bp_i_0,bp_i_1+prices[i])
            bp_i_1=max(bp_i_1,tmp-prices[i])
        return bp_i_0
s=Solution()
print(s.maxProfit([1,2,3,4,5]))

