# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
        
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        node_list = []
        def preorder(node: Optional[TreeNode]) -> None:
            if not node:
                return 

            node_list.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ",".join(node_list)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        preorder_list = list(map(int, data.split(",")))

        def build_bst(bounds = (float("-inf"), float("inf"))):
            if preorder_list and bounds[0] < preorder_list[0] < bounds[1]:
                val = preorder_list.pop(0)
                node = TreeNode(val)
                node.left = build_bst((bounds[0], val))
                node.right = build_bst((val, bounds[1]))
                return node

            return None

        return build_bst()

        
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans