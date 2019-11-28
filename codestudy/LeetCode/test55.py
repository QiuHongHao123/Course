class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenth=len(nums)
        sum =0
        ans=nums[0]
        for i in range(0,lenth):

            if sum>0:
                sum=sum+nums[i]

            else:
                sum = nums[i]
            ans=max(ans,sum)

        return ans
