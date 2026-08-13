class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        left = 0.0
        right = max(stations[i] - stations[i - 1]
                    for i in range(1, len(stations)))

        while right - left > 1e-6:

            mid = (left + right) / 2

            count = 0

            for i in range(1, len(stations)):
                gap = stations[i] - stations[i - 1]

                count += math.ceil(gap / mid) - 1

            if count <= k:
                right = mid
            else:
                left = mid

        return right

    