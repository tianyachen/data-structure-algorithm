class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False

        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(total: int) -> bool:
            if total == target:
                return True
            
            if total in seen or total < 0 or total > x + y:
                return False
            
            seen.add(total)

            for direction in directions:
                jug1 = direction[0] * x
                jug2 = direction[1] * y
                if dfs(total + jug1 + jug2):
                    return True
            
            return False

        return dfs(0)
