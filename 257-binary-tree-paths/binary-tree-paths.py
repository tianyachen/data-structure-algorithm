# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None: 
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        path: List[str] = []
        ans: List[str] = []

        def dfs(node: Optional[TreeNode], path: List[str]) -> None:
            if node is None:
                return
            # leaf node
            if node.left is None and node.right is None:
                path.append("->")
                path.append(str(node.val))
                ans.append("".join(path))
                return
            
            path.append("->")
            path.append(str(node.val))
            if node.left is not None:
                dfs(node.left, path)
                path.pop()
                path.pop()
            if node.right is not None:
                dfs(node.right, path)
                path.pop()
                path.pop()


        dfs(root.left, [str(root.val)])
        dfs(root.right, [str(root.val)])
        return ans
