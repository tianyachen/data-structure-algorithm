class MyLinkedList {
    ListNode head;
    ListNode tail;
    int size;

    public MyLinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
    
    public int get(int index) {
        ListNode node = getNodeAtIndex(index);
        if (node != null) {
            return node.val;
        }
        return -1;
    }
    
    public void addAtHead(int val) {
        if (this.size == 0) {
            addFirstNode(val);
            this.size++;
            return;
        }
        ListNode newHead = new ListNode(val, this.head, null);
        this.head.prev = newHead;
        this.head = newHead;
        this.size++;
    }
    
    public void addAtTail(int val) {
        if (this.size == 0) {
            addFirstNode(val);
            this.size++;
            return;
        }
        ListNode newTail = new ListNode(val, null, this.tail);
        this.tail.next = newTail;
        this.tail = newTail;
        this.size++;
    }
    
    public void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
        }
        else if (index == this.size) {
            addAtTail(val);
        }
        else if (isWithinBound(index)) {
            ListNode node = getNodeAtIndex(index);
            ListNode newNode = new ListNode(val, node, node.prev);
            node.prev.next = newNode;
            node.prev = newNode;
            this.size++;
        }
        
    }
    
    public void deleteAtIndex(int index) {
        ListNode node = getNodeAtIndex(index);
        if (node == null) return;
        
        if (this.size == 1) {
            this.head = null;
            this.tail = null;
        } else if (node == head) {
            node.next.prev = null;
            this.head = node.next;
        } else if (node == tail) {
            node.prev.next = null;
            this.tail = node.prev;
        }
        else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }
        this.size--;
    }
    
    private boolean isWithinBound(int index) {
        return index >= 0 && index < this.size;
    }
    
    private ListNode getNodeAtIndex(int index) {
        if (!isWithinBound(index)) return null;

        ListNode cur = this.head;
        for (int i = 0; i < index; i++) {
            cur = cur.next;
        }
        return cur;
    }
    
    private void addFirstNode(int val) {
        ListNode node = new ListNode(val);
        this.head = node;
        this.tail = node;
    }
    
    @Override
    public String toString() {
        ListNode cur = this.head;
        StringBuilder ret = new StringBuilder();
        
        while (cur != null) {
            ret.append(cur.val);
            ret.append(" ");
            cur = cur.next;
        }
        return ret.toString();
    }
    
    private class ListNode {
        int val;
        ListNode next;
        ListNode prev;
        ListNode() {
            this.val = 0;
            this.next = null;
            this.prev = null;
        }
        ListNode(int val) {
            this();
            this.val = val;
        }
        ListNode(int val, ListNode next, ListNode prev) {
            this.val = val;
            this.next = next;
            this.prev = prev;
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */