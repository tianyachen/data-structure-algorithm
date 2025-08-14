# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode]) -> Tuple[TreeNode, int]:
            if not node:
                return (None, 0)

            leftNode, leftDepth = dfs(node.left)
            rightNode, rightDepth = dfs(node.right)

            if leftDepth == rightDepth:
                return (node, leftDepth + 1)
            elif leftDepth > rightDepth:
                return (leftNode, leftDepth + 1)
            
            return (rightNode, rightDepth + 1)


        retNode, _ = dfs(root)
        return retNode