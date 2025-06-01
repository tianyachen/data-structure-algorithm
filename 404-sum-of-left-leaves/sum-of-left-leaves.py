# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        isLeft = False

        def leftSum(node: Optional[TreeNode], isLeft: bool) -> int:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                if isLeft:
                    return node.val
                else:
                    return 0

            return leftSum(node.left, True) + leftSum(node.right, False)

        return leftSum(root, isLeft)