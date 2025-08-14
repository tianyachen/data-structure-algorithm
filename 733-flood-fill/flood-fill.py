class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image
            
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col) -> None:
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            if image[row][col] != original_color:
                return

            image[row][col] = color

            for r, c in directions:
                dfs(row + r, col + c)

        dfs(sr, sc)
        return image
            
        
        