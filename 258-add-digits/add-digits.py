class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while ans > 9:
            num = ans
            ans = 0
            while num > 0:
                ans += num % 10
                num //= 10

        return ans