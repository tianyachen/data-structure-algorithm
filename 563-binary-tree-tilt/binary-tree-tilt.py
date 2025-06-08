# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node):
            if node is None:
                return 0

            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            self.total += abs(leftSum - rightSum)

            return leftSum + node.val + rightSum

        dfs(root)
        return self.total