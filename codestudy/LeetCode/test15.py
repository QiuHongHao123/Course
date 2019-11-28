from typing import List
class Solution:
    def threeSum(self, nums : List[int]) :
        #三数之和，先排序再用双指针

        nums.sort()
        answers=[]
        for i in range(0,len(nums)):
            j=i+1
            k=len(nums)-1
            subnum=int                                          #subnum用以存储之前的num[j]防止出现重复元组
            #由于排序后从小到大故如果nums[i]>0那么和也一定大于0
            if nums[i]>0: break
            #防止重复元组进入
            if i>0 and nums[i]==nums[i-1]: continue
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    if nums[j]!=subnum:
                        answers.append([nums[i],nums[j],nums[k]])
                    subnum=nums[j]
                    j+=1
                    k-=1
                    #和大于0代表需减小所以k--
                elif s>0:
                    k-=1
                else:
                    j+=1
        return answers

s=Solution()
print(s.threeSum([3,0,-2,-1,1,2]))

