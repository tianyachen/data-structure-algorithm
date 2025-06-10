class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {word : i for i, word in enumerate(list1)}
        min_sum = float("inf")
        ans = []

        for j in range(len(list2)):
            if list2[j] in index_map:
                cur_sum = index_map[list2[j]] + j

                if cur_sum < min_sum:
                    min_sum = cur_sum
                    ans = [list2[j]]

                elif cur_sum == min_sum:
                    ans.append(list2[j])

        return ans