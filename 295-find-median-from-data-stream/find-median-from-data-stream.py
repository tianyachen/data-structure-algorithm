class MedianFinder:

    def __init__(self):
        self.orderedList = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.orderedList, num)

    def findMedian(self) -> float:
        n = len(self.orderedList)
        if n % 2 == 0:
            print(n)
            return (self.orderedList[n // 2 - 1] + self.orderedList[n//2]) / 2
        else:
            return float(self.orderedList[n // 2])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()