# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from numbers import Number
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float("inf")

        def dfs(node):
            if node:
                dfs(node.left)
                if self.prev is not None:
                    self.ans = min(self.ans, node.val-self.prev)
                self.prev = node.val
                dfs(node.right)

        dfs(root)
        return self.ans