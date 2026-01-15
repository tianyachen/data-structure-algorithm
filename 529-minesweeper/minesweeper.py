class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])

        r, c = click

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        def count_mines(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if board[nx][ny] == 'M':
                        count += 1
            return count

        def dfs(x, y):
            if board[x][y] != 'E':
                return

            mines = count_mines(x, y)

            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        dfs(nx, ny)



        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)

        return board
            

        