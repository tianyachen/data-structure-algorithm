# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        array = []
    
        def helper(node) -> None:
            if node is None:
                return 
            helper(node.left)
            array.append(node.val)
            helper(node.right)

        helper(root)

        left = 0
        right = len(array) - 1

        while left < right:
            s = array[left] + array[right]

            if s == k:
                return True
            elif s < k:
                left += 1
            else:
                right -= 1

        return False
        