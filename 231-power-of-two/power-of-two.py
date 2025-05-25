class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0 :
            return False
        
        low = 0
        high = math.ceil(n ** 0.5) 

        while low < high:
            mid = low + (high - low) // 2

            if 2 ** mid < n:
                low = mid + 1
            else:
                high = mid

        return 2 ** low == n