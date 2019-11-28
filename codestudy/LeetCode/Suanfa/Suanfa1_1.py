from typing import List
def getMediand(nums1:List[int],nums2:List[int])->int:
    #传入两个相同大小的有序数组找到其中位数
    lenth=len(nums1)
    imax=lenth
    imin=0
    while imin<imax:
        i=(imin+imax)//2
        j=lenth-i
        if nums1[i-1]>nums2[j] and i>0:
            imin=i+1
        elif nums2[j-1]>nums2[i] and i<lenth:
            imax=i-1
        else:
            break
    if i == 0 :
        maxLeft = nums2[j-1]
    elif j == 0:
        maxLeft = nums1[i-1];
    else :
        maxLeft = max(nums1[i-1], nums2[j-1])
    if (i == lenth):
        minRight = nums2[j]
    elif (j == lenth):
        minRight = nums1[i]
    else:
        minRight = min(nums2[j], nums1[i])

    return (maxLeft+minRight)/2
print(getMediand([1,3],[2,5]))