class TimeMap:

    def __init__(self):
        self.tmap: Dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        search = self.tmap.get(key, []) # LIST of pairs
        l = 0
        r = len(search) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
    
            if search[m][1] <= timestamp:
                res = search[m][0]
                l = m + 1
            else:
                r = m - 1
            
        return res

