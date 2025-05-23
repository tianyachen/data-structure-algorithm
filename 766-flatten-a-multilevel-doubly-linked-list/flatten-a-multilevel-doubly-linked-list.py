"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: 
            return None
        dummy = Node(0)
        cur = dummy 
        stack = [head]
        
        while stack:
            tmp = stack.pop()
            if tmp.next:
                stack.append(tmp.next)
            if tmp.child:
                stack.append(tmp.child)
            cur.next = tmp
            tmp.prev = cur
            tmp.child = None
            cur = tmp
            
        dummy.next.prev = None
        return dummy.next