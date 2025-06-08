class Solution {
    public String[] findRelativeRanks(int[] score) {
        int N = score.length;

        PriorityQueue<Pair<Integer, Integer>> maxHeap = new PriorityQueue<>((a,b) -> b.getKey() - a.getKey());

        for (int i = 0; i < N; i++) {
            maxHeap.offer(new Pair(score[i], i));
        }

        String[] rank = new String[N];
        int place = 1;
        while (!maxHeap.isEmpty()) {
            int index = maxHeap.poll().getValue();
            if (place == 1) {
                rank[index] = "Gold Medal"; 
            } else if (place == 2) {
                rank[index] = "Silver Medal";
            } else if (place == 3) {
                rank[index] = "Bronze Medal";
            } else {
                rank[index] = String.valueOf(place);
            }
            place++;
        }
        return rank;

    }
}