class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        ans = []
        isNegative = num < 0
        num = abs(num)

        while num:
            ans.append(str(num % 7))
            num //= 7

        result = "".join(ans[::-1])
        return '-' + result if isNegative else result