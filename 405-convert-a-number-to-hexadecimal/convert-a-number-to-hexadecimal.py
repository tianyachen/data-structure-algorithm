class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        ans = []
        num &= 0xFFFFFFFF
        while num:
            remainder = num % 16
            if remainder > 9:
                ans.append(chr(ord('a') + remainder - 10))
            else:
                ans.append(str(remainder))
            num //= 16

        return "".join(ans[::-1])