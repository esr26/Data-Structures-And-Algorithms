class TimeMap:

    def __init__(self):
        self.timeHash = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeHash[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timeHash:
            return ""
        
        lst = self.timeHash[key]
        left = 0
        right = len(lst)-1

        while left <= right:
            mid = (left + right) // 2

            if lst[mid][1] == timestamp:
                return lst[mid][0]
            
            elif lst[mid][1] > timestamp:
                right = mid - 1
            
            else:
                left = mid + 1
        
        if right >= 0:
            return lst[right][0]
        
        return ""
            



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)