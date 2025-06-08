"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: 
            return 0

        maxLen = 1
        for child in root.children:
            maxLen = max(maxLen, self.maxDepth(child) + 1)

        return maxLen