# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        res=[]
        if root.val not in to_delete:
            res.append(root)
        def dfs(node):
            if node is None:
                return False
            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    res.append(node.left)
                if node.right and node.right.val not in to_delete:
                    res.append(node.right)
            if dfs(node.left):
                node.left=None
            if dfs(node.right):
                node.right=None
            return node.val in to_delete
            
        
        dfs(root)
        return res
            