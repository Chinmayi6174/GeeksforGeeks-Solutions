'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def correctBST(self, root):
        self.first= None
        self.second= None
        self.prev=None
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.data > node.data:
                if not self.first:
                    self.first= self.prev
                self.second=node
            self.prev = node
            inorder(node.right)
        inorder(root)
        self.first.data, self.second.data = self.second.data, self.first.data
