class Solution:
    def maxArea(self, height) :
        #找最大水池容量“双指针法”
        lenth=len(height)
        i=0
        j=lenth-1
        marea=0
        while j>i:
            area=min(height[i],height[j])*(j-i)
            if area>marea: marea=area
            if height[i]>height[j]:
                j-=1
            else:
                i+=1


        return marea

s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))





