from typing import List
def knapsack(itemsv:List,itemsw:List,capacity:int )-> int:
    # knapsack (Original situation)
    lenth=len(itemsv)
    dp=[[0]*(capacity+1) for i in range(lenth)]

    for i in range(0, lenth):
        for j in range(1,capacity+1):
            if (itemsw[i] >= j):
                dp[i][j]=dp[i - 1][j]
            else:
                dp[i][j]=max(itemsv[i] + dp[i - 1][j - itemsw[i]],dp[i-1][j])
    return dp[i][j]

print(knapsack([3,4,5,6],[2,3,4,5], 9))
def knapsack1(itemsv:List,itemsw:List,n:List,capacity:int)->int:
    lenth=len(itemsv)

    dp = [[0] *(capacity+1) for i in range(lenth + 1)]
    for i in range(1, lenth + 1):
        for j in range(1, capacity + 1):

            max_num = min(j / itemsw[i - 1], n[i - 1])

            dp[i][j] = dp[i - 1][j]
            for k in range(max_num + 1):
                if dp[i][j] < dp[i - 1][j - k *itemsw[i - 1]] + k * itemsv[i - 1]:
                    dp[i][j] = dp[i - 1][j - k * itemsw[i - 1]] + k * itemsv[i - 1]

    return dp[i][j]

