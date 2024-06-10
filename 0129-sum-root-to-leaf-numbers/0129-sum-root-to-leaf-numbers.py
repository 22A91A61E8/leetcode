# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def divya(self, root, s, total_sum):
        if root is None:
            return
        if root.left is None and root.right is None:
            total_sum[0] += (s * 10 + root.val)
            return
        self.divya(root.left, s * 10 + root.val, total_sum)
        self.divya(root.right, s * 10 + root.val, total_sum)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = [0]
        self.divya(root, 0, total_sum)
        return total_sum[0]
