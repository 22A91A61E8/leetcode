"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack=[root]
        l=[]
        while stack:
            r=stack.pop()
            l.append(r.val)
            stack.extend(r.children)
        return l[::-1]
            
  