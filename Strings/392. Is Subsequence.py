class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s: 
            return True
            

        index = 0
        for i in range(len(t)):

            if s[index] == t[i]:
                index += 1
                if index == len(s): 
                    return True

        return False

