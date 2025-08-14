class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            digits = self.getDigits(num)
            if self.isSelfDividing(digits, num):
                ans.append(num)

        return ans

    def getDigits(self, num) -> List[int]:
        ans = []
        while num > 0:
            ans.append(num % 10)
            num //= 10

        return ans

    def isSelfDividing(self, digits, num) -> bool:
        for digit in digits:
            if digit == 0 or num % digit != 0:
                return False

        return True