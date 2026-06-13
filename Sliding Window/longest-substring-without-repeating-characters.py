class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0

        left = 0

        charset = set()

        for right in range(len(s)):

            while s[right] in charset:
                charset.remove(s[left])
                left += 1
                
            charset.add(s[right])

            
            longest = max(right-left+1, longest)

                
        
        return longest
        