from typing import List
sum=0
def inversion(nums:List[int]):
    lenth = len(nums)
    global sum
    if lenth == 1:
        return nums
    else:
        left=inversion(nums[0:lenth//2])
        right= inversion(nums[lenth//2:])
        rlist=[]
        i=0
        j=0
        while i<len(left)and j<len(right):
            if(left[i]<right[j]):
                rlist.append(left[i])
                i+=1
            else:
                rlist.append(right[j])
                sum+=len(left)-i
                j+=1

        for i in range(i,len(left)):
            rlist.append(left[i])
        for j in range(j,len(right)):
            rlist.append(right[j])
        return rlist
#inversion([1,2,3,4,5,6,7,0])
inversion([4,3,2])
print(sum)

