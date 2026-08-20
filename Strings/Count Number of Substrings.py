class Solution:
    def countSubstr(self, s, k):
        
        def atMost(k):
            count = {}
            left = 0
            res = 0

            for right in range(len(s)):
                ch = s[right]
                count[ch] = count.get(ch, 0) + 1

                while len(count) > k:
                    left_ch = s[left]
                    count[left_ch] -= 1

                    if count[left_ch] == 0:
                        del count[left_ch]

                    left += 1

                # Every substring ending at right
                # from left to right is valid
                res += right - left + 1

            return res

        return atMost(k) - atMost(k - 1)