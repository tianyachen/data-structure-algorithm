class Solution:
    def checkRecord(self, s: str) -> bool:
        totalAbsent = 0
        consecutiveLate = 0

        for c in s:
            if c == "A":
                totalAbsent += 1
                consecutiveLate = 0
            elif c == "L":
                consecutiveLate += 1
            else:
                consecutiveLate = 0

            if consecutiveLate >= 3:
                return False
            if totalAbsent >= 2:
                return False

        return True
                