class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = duration

        for i in range(len(timeSeries) - 2, -1, -1):
            if timeSeries[i] + duration - 1 < timeSeries[i + 1]:
                count += duration
            else:
                count += timeSeries[i + 1] - timeSeries[i]

        return count