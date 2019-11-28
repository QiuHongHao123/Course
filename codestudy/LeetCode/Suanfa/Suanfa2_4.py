from typing import List
#分词权值
def quality(String: List):
    return 0
def  dividewords(String:List):
    divided=[]
    length=len(String)
    if length==1:
        divided.append(String)
        return quality(String),divided

    maxquality=0
    for i in range(length-1,-1,-1):
        nquality,tmplist=dividewords(String[:i])
        if maxquality<nquality+quality(String[i:]):
            maxquality=nquality+quality(String[i:])
            divided=tmplist.append(String[i:])

    return maxquality,divided
