class Solution {
    public int nthUglyNumber(int n) {
        PriorityQueue<Long> minHeap = new PriorityQueue<>();
        minHeap.offer(1L);
        Set<Long> seen = new HashSet<>();
        long num = 0;
        int[] factors = {2, 3, 5};
        for (int i = 0; i < n; i++) {
            num = minHeap.poll();
            if (i == n - 1) {
                break;
            }
            for (int factor : factors) {
                long newNum = factor * num;
                if (!seen.contains(newNum)) {
                    seen.add(newNum);
                    minHeap.offer(newNum);
                }
            }
        }
        return (int) num;

    }
}