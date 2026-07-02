class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1

        x = abs(x)
        rev = 0

        while x:
            val = x % 10
            x //= 10
            rev = rev * 10 + val
        
        rev *= sign

        if rev > (2**31 - 1) or rev < (-2**31):
            return 0
        
        return rev