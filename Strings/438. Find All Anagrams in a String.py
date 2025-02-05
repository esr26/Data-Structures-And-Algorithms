from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n, m = len(s), len(p)
        
        # Edge case: if the length of p is greater than s, no anagrams can exist
        if n < m:
            return res
        
        # Counter for the characters in p
        count_p = Counter(p)
        
        # Initialize a sliding window of size m for the string s
        window = Counter(s[:m])
        
        # Compare the initial window with count_p
        if window == count_p:
            res.append(0)
        
        # Slide the window across s
        for i in range(1, n - m + 1):
            # Remove the character going out of the window
            window[s[i - 1]] -= 1
            if window[s[i - 1]] == 0:
                del window[s[i - 1]]
            
            # Add the new character coming into the window
            window[s[i + m - 1]] += 1
            
            # Compare the current window with count_p
            if window == count_p:
                res.append(i)
        
        return res
