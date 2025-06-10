# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        val1 = 0
        val2 = 0
        left1 = None
        left2 = None
        right1 = None
        right2 = None
        if root1:
            val1 = root1.val 
            left1 = root1.left
            right1 = root1.right
        if root2:
            val2 = root2.val
            left2 = root2.left
            right2 = root2.right
        
        newNode = TreeNode(val = val1 + val2)

        newNode.left = self.mergeTrees(left1, left2)
        newNode.right = self.mergeTrees(right1, right2)
        return newNode