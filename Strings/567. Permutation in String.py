class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        if n < m: return False

        count_s1 = Counter(s1)
        window = Counter(s2[:m])

        if window == count_s1: return True

        for i in range(1, n-m+1):
            window[s2[i-1]] -= 1
            if window[s2[i-1]] == 0:
                del window[s2[i-1]]
            
            window[s2[i+m-1]] += 1
            if window == count_s1:
                return True
        return False

