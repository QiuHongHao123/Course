class Solution:
    #非递归层次遍历
    def maxDepth(self, root) :
        list=[]
        depth=0
        if root==None:
            return 0
        list.append(root)

        while list:
            size=len(list)
            depth+=1
            for i in range(0,size):
                p=list.pop(0)
                if p.left!=None:
                    list.append(p.left)
                if p.right!=None:
                    list.append(p.right)
        return depth


