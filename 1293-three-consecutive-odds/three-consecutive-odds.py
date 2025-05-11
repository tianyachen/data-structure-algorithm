class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        
        for i in range(n):
            if arr[i] % 2 == 0:
                continue
            
            if i + 1 < n and arr[i + 1] % 2 == 1 and i + 2 < n and arr[i + 2] % 2 == 1:
                return True

        return False