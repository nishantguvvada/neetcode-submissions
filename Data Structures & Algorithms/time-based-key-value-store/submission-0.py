class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, [])
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys() or timestamp < self.store[key][0][0]:
            return ""
        left = 0
        right = len(self.store[key]) - 1
        best = ""

        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][0] <= timestamp:
                best = self.store[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return best
