class Solution:
    def aggressiveCows(self, stalls: List[int], k: int) -> int:

        stalls.sort()

        left = 1
        right = stalls[-1] - stalls[0]
        ans = 0

        while left <= right:

            mid = (left + right) // 2

            # Can we place k cows with at least
            # 'mid' distance between them?
            count = 1
            last = stalls[0]

            for stall in stalls[1:]:
                if stall - last >= mid:
                    count += 1
                    last = stall

            if count >= k:
                # mid works -> try a larger distance
                ans = mid
                left = mid + 1
            else:
                # mid doesn't work -> try smaller distance
                right = mid - 1

        return ans

    