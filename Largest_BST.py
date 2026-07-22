class Solution:
    def largestBst(self, root):
        self.maxsize = 0
        def helper(node):
            # Returns:
            # (isBST, size, minVal, maxVal)
            if not node:
                return (True, 0, float('inf'), float('-inf'))

            left_isBST, left_size, left_min, left_max = helper(node.left)
            right_isBST, right_size, right_min, right_max = helper(node.right)

            # Check BST property
            if left_isBST and right_isBST and left_max < node.data < right_min:

                curr_size = left_size + right_size + 1

                self.maxsize = max(self.maxsize, curr_size)

                curr_min = min(left_min, node.data)
                curr_max = max(right_max, node.data)

                return (True, curr_size, curr_min, curr_max)

            # Not a BST
            return (False, 0, 0, 0)

        helper(root)

        return self.maxsize
