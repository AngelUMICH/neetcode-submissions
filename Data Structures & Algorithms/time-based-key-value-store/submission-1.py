class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res,items = "", self.data.get(key, [])
        l,r = 0, len(items)-1
        while r >= l:
            mid = (r+l)//2
            if items[mid][1] <= timestamp:
                res = items[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
