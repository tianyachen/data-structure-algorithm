# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans
        
    def helper(self, node: Optional[TreeNode], collection: List[int]) -> None:
        if node is None:
            return
        
        self.helper(node.left, collection)
        collection.append(node.val)
        self.helper(node.right, collection)