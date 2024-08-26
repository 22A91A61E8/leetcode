# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l=[]
        s=[root]
        while s:
            r=s.pop()
            l.append(r.val)
            if r.right:
                s.append(r.right)
            if r.left:
                s.append(r.left)
        return l