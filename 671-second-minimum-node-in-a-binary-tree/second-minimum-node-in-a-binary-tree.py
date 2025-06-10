# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        self.min_val = root.val
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            if self.min_val < node.val < self.ans:
                self.ans = node.val
            elif node.val == self.min_val:
                dfs(node.left)
                dfs(node.right)
            

        dfs(root)
        return self.ans if self.ans != float("inf") else -1