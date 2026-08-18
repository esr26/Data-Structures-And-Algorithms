class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)
        bucket = [[] for _ in range(len(s) + 1)]

        for ch, count in freq.items():
            bucket[count].append(ch)
        
        res = []

        for count in range(len(s), 0, -1):
            for ch in bucket[count]:
                res.append(ch * count)
            
        return "".join(res)




    