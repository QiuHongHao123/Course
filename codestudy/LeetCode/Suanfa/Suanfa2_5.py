#带权活动安排
from typing import List

def maxweight(activity:List[List])->int:
    nact=sorted(activity,key=lambda x:x[1])
    lenth=len(nact)
    maxweight=[0]*lenth
    maxweight[0]=nact[0][2]
    for i in range(1,lenth):
        last=-1
        for j in range(0,lenth):
            if nact[j][1]>=nact[i][0]:
                break
            else:
                last=j
        if last==-1:
            maxweight[i]=max(nact[i][2],maxweight[i-1])
        else:
            maxweight[i]=max(maxweight[last]+nact[i][2],maxweight[i-1])

    return maxweight
print(maxweight([[1,4,2],[7,10,3],[2,6,8]]))