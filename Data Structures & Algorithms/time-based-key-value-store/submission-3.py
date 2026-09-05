class TimeMap:

    def __init__(self):
        # each key stores -> list of [timestamp, value]
        self.store = {}
        # alice = [[happy, 1], [sad, 3], [happy, 5]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]

        res = ""
        l, r = 0, len(values)-1
        #[1, 5, 10, 14, 20]
        while l <= r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            elif values[m][1] > timestamp:
                r = m-1
        return res








        
