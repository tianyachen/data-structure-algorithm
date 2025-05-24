class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        Map<Integer, Integer> numToIdx = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num1 = nums[i];
            int num2 = target - num1;
            if (numToIdx.containsKey(num2)) {
                ans[0] = numToIdx.get(num2);
                ans[1] = i;
                break;
            } else {
                numToIdx.put(num1, i);
            }

        }
        return ans;
    }
}