'''
找最少基站数
'''
from typing import List
'''
输入为船点集，第一个元素为横坐标第二个元素为纵坐标
'''
def get_min_J(P:List[List],d):
    new_P=sorted(P,key=lambda p : p[0])
    print(new_P)
    Jcount=0
    while new_P!=[]:
        x=pow(pow(d,2)-pow(new_P[0][1],2),0.5)
        J_x=new_P[0][0]+x
        new_P.pop(0)
        tmpnew_P=new_P
        for p in new_P:
            if pow(p[0]-J_x,2)+pow(p[1],2)<=pow(d,2):
                tmpnew_P.remove(p)

        new_P=tmpnew_P
        print(new_P)
        Jcount+=1
    return Jcount
print(get_min_J([[0,2],[1,1],[1,0.5],[2,1],[2,0.5],[3,2],[10,2]],2))
