# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode], depth: int) -> Tuple[TreeNode, int]:
            if not node:
                return (None, depth)

            leftNode, leftDepth = dfs(node.left, depth + 1)
            rightNode, rightDepth = dfs(node.right, depth + 1)

            if leftDepth == rightDepth:
                return (node, leftDepth)
            elif leftDepth > rightDepth:
                return (leftNode, leftDepth)
            
            return (rightNode, rightDepth)


        retNode, _ = dfs(root, 0)
        return retNode