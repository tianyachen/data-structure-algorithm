# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return None
        
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None

        prev = None
        curr = secondHalf

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        reversedHalf = prev

        curr1 = head
        curr2 = reversedHalf

        while curr1 and curr2:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2
        