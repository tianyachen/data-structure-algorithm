class Solution:
    def judgeCircle(self, moves: str) -> bool:
        leftCount = 0
        rightCount = 0
        upCount = 0
        downCount = 0

        for move in moves:
            match move:
                case 'L':
                    leftCount += 1
                case 'R':
                    rightCount += 1
                case 'U':
                    upCount += 1
                case 'D':
                    downCount += 1

        return leftCount == rightCount and upCount == downCount