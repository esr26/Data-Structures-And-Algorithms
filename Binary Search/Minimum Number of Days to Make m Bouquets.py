class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left <= right:

            mid = (left + right) // 2

            cnt = 0
            need = 0

            for num in bloomDay:
                if num <= mid:
                    cnt += 1
                else:
                    need += cnt // k
                    cnt = 0

            need += cnt // k

            if need >= m:
                right = mid - 1
            else:
                left = mid + 1

        return left