class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        timeseries = self.store[key]
        idx = bisect.bisect_left(timeseries, timestamp, key= lambda x: x[1])
        timeseries.insert(idx, (value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        timeseries = self.store[key]
        idx = bisect.bisect_left(timeseries, timestamp, key = lambda x: x[1])
        if len(timeseries) == 0 or (idx == 0 and timestamp < timeseries[idx][1]):
            return ""
        elif idx >= len(timeseries) or timestamp < timeseries[idx][1]:
            return timeseries[idx - 1][0]
        else:
            return timeseries[idx][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)