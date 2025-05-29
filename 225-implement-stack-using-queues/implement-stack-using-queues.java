class MyStack {
    Queue<Integer> store;
    Queue<Integer> retrieve;
    public MyStack() {
        store = new LinkedList<>();
        retrieve = new LinkedList<>();
    }
    
    public void push(int x) {
        retrieve.offer(x);
    }
    
    public int pop() {
        int elem;
        while (retrieve.size() > 1) {
            elem = retrieve.poll();
            store.offer(elem);
        }
        int ret = retrieve.poll();
        Queue<Integer> temp = store;
        store = retrieve;
        retrieve = temp;
        return ret;
    }
    
    public int top() {
        int elem;
        while (retrieve.size() > 1) {
            elem = retrieve.poll();
            store.offer(elem);
        }
        int ret = retrieve.poll();
        store.offer(ret);
        Queue<Integer> temp = store;
        store = retrieve;
        retrieve = temp;
        return ret;
    }
    
    public boolean empty() {
        return retrieve.size() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */