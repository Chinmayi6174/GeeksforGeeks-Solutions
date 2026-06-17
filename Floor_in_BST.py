'''Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None'''
class Solution:
    def findMaxFork(self, root, k):
        #code here
        ans=-1
        curr=root
        while curr:
            if curr.data==k:
                return curr.data
            if curr.data<k:
                ans=curr.data
                curr= curr.right
            else:
                curr=curr.left
        return ans
