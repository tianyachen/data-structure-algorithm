class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n:
            return mat

        newMat = [[0] * c for _ in range(r)]
        col = 0
        row = 0
        for i in range(m):
            for j in range(n):
                if col == c:
                    row += 1
                    col = 0

                newMat[row][col] = mat[i][j]
                col += 1
                
        return newMat