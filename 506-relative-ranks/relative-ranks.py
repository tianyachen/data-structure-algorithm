class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse = True)
        rank = {}

        for i in range(len(sortedScore)):
            s = sortedScore[i]
            if i == 0:
                rank[s] = "Gold Medal"
            elif i == 1:
                rank[s] = "Silver Medal"
            elif i == 2:
                rank[s] = "Bronze Medal"
            else:
                rank[s] = str(i + 1)

        ans = []
        for i in range(len(score)):
            ans.append(rank[score[i]])

        return ans