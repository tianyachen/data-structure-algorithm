/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return null;
        if (k < 1) return head;
        int n = 1;
        ListNode tail;
        ListNode cur = head;
        
        while (cur.next != null) {
            n++;
            cur = cur.next;
        }
        tail = cur;

        int leftPart = n - (k % n);
        if (leftPart == n) return head;
        ListNode dummy = new ListNode(0, head);
        cur = dummy;
        for (int i = 0; i < leftPart; i++) {
            cur = cur.next;
        }
        dummy.next = cur.next;
        tail.next = head;
        cur.next = null;
        return dummy.next;
    }
}