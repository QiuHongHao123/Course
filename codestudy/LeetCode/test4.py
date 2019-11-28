class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m= len(nums1)
        n = len(nums2)

        if n<m :
            t=n
            numt=nums1
            n=m
            m=t
            nums1=nums2
            nums2=numt

        imax = m
        imin = 0
        while imin<=imax:
            i = (imax + imin) //2
            j=(n+m+1-2*i)//2
            if i==0 or i==m:
                break
            if(nums1[i-1]<=nums2[j] or nums1[i]>=nums2[j-1]):
                break
            if nums1[i-1]>nums2[j]:
                imax=i-1
            if nums1[i]<nums2[j-1]:
                imin=i+1
        if i == 0:
            max_of_left = nums2[j - 1]
        elif j == 0:
            max_of_left = nums1[i - 1]
        else:
            max_of_left = max(nums1[i - 1],nums2[j - 1])

        if (m + n) % 2 == 1:
            return max_of_left

        if i == m:
            min_of_right = nums2[j]
        elif j == n: min_of_right = nums1[i]
        else:
            min_of_right = min(nums1[i], nums2[j])

        return (max_of_left + min_of_right) / 2.0




s=Solution()
print(s.findMedianSortedArrays([1,3],[2]))



