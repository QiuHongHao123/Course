'''
黑白点最短路
'''
from typing import List
'''
传入为点集黑点为-1白点为1
'''
def minlen_between_black_white(nodes:List):
    unconnect=len(nodes)
    trance=0
    distance=1
    while unconnect!=0:
        for i in range(len(nodes)):
            if nodes[i]!=0:
                if i+distance<len(nodes)and nodes[i+distance]==-nodes[i]:
                    nodes[i]=0
                    nodes[i+distance]=0
                    unconnect-=2
                    trance+=distance
        distance+=1
    return trance
print(minlen_between_black_white([-1,-1,1,-1,1,1,1,-1]))



