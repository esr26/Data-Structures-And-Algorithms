class Solution:
    def kthElement(self, a, b, k):

        # Always binary search on the smaller array
        if len(a) > len(b):
            a, b = b, a

        m = len(a)
        n = len(b)

        # Number of elements we can take from a
        left = max(0, k - n)
        right = min(k, m)

        while left <= right:

            # Number of elements taken from a
            cut1 = (left + right) // 2

            # Remaining elements needed from b
            cut2 = k - cut1

            # Boundary values around the partition
            left1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
            right1 = float('inf') if cut1 == m else a[cut1]

            left2 = float('-inf') if cut2 == 0 else b[cut2 - 1]
            right2 = float('inf') if cut2 == n else b[cut2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)

            # Too many elements taken from a
            elif left1 > right2:
                right = cut1 - 1

            # Too few elements taken from a
            else:
                left = cut1 + 1

        return -1

    