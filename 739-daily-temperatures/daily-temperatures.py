class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, prevIdx = stack.pop()
                ans[prevIdx] = i - prevIdx

            stack.append((temp, i))
        
        return ans