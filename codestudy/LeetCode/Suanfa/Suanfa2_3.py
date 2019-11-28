#树涂色
from typing import List
class getmaxblack():
    nodes=[]
    def __init__(self,nodes:List[List]):
        self.nodes=nodes
    def init_situation(self):

        initwhite,wlist=self.maxblack(0,0)                                            #根节点为白
        initblack,blist=self.maxblack(1,0)                                            #根节点为黑
        initblack+=1
        blist+=[0]

        if initblack>initwhite:
            return initblack,blist
        else:
            return initwhite,wlist
    def maxblack(self,flag:int,i:int):
        maxsum=0
        leaveflag=1
        blacklist=[]
        for k in range(len(self.nodes[i])):
                if self.nodes[i][k]==1:
                    leaveflag=0
                    if flag==0:
                        if self.maxblack(0,k)>self.maxblack(1,k):
                            tmp,tmplist=self.maxblack(0,k)
                            maxsum+=tmp
                            blacklist+=tmplist
                        else:
                            tmp, tmplist = self.maxblack(1, k)
                            maxsum += tmp
                            blacklist += tmplist

                    else:
                        tmp, tmplist = self.maxblack(1, k)
                        maxsum += tmp
                        blacklist += tmplist

        if leaveflag==0:
            return maxsum,blacklist
        else:
            if flag==1:
                return 1,[i]
            else:
                return 0,[]



gb=getmaxblack([[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
gb=getmaxblack([[0,1,0,0,0],[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
print(gb.init_situation())



