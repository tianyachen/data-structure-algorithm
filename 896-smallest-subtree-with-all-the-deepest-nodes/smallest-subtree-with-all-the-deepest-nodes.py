# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        queue = deque([root])
        parents = {root: None}

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                if node.left:
                    parents[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parents[node.right] = node
                    queue.append(node.right)

        nodes = set(current_level)
        while len(nodes) > 1:
            nodes = set(parents[node] for node in nodes)

        return nodes.pop()

            