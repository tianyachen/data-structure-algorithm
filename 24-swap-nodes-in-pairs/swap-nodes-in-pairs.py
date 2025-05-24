# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(node):
            if not node or not node.next:
                return node
            n, nn = node.next, node.next.next
            n.next = node
            node.next = recursion(nn)
            return n
        return recursion(head)