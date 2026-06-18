# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None
# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        #your code here
        self.count=0
        self.ans=None
        def reverse_inorder(node):
            if not node or self.ans is not None:
                return
            reverse_inorder(node.right)
            self.count+=1
            if self.count==k:
                self.ans=node.data
                return
            reverse_inorder(node.left)
        reverse_inorder(root)
        return self.ans
