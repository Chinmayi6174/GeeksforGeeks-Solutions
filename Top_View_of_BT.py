'''class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None'''
class Solution:
    def topView(self, root):
        # code here
        q=deque([(0,root)])
        d={}
        while(len(q)>0):
            vertical,node= q.popleft()
            if(node.left):
                q.append((vertical-1,node.left))
            if(node.right):
                q.append((vertical+1,node.right))
            if(vertical not in d):
                d[vertical]=node.data
        ans=[]
        for i in sorted(d):
            ans.append(d[i])
        return ans
