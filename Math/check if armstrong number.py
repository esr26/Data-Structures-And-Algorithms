class Solution:

    def countDigits(self, num):
        if num == 0:
            return 1

        count = 0
        while num:
            count += 1
            num //= 10
        return count

    def isArmstrong(self, n: int) -> bool:
        power = self.countDigits(n)
        total = 0
        temp = n

        while temp:
            digit = temp % 10
            total += digit ** power
            temp //= 10

        return total == n
    