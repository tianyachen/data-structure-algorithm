class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
            
        m = len(image)
        n = len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(sr, sc)])

        while queue:
            r, c = queue.popleft()

            if image[r][c] == original_color:
                image[r][c] = color

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original_color:
                        queue.append((nr, nc))
            
        return image
            
        
        