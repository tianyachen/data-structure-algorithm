class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        visited = set()
        cycle = set()
        ans = []
        for prerequisite in prerequisites:
            adj_list[prerequisite[0]].append(prerequisite[1])

        def dfs(i: int) -> bool:
            if i in cycle:
                return False
            if i in visited:
                return True

            cycle.add(i)
            for pre in adj_list[i]:
                if not dfs(pre):
                    return False
            cycle.remove(i)
            visited.add(i)
            ans.append(i)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ans
        
