class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = floor(sqrt(area))
        while w > 0 and area % w != 0:
            w -= 1
        
        l = area // w

        return [l, w]
