class Solution:
    def countOccurrences(self, nums: List[int], target: int) -> int:

        def findFirst():
            left = 0
            right = len(nums) - 1
            res = -1

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    res = mid

                    # Search further left
                    right = mid - 1

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return res


        def findLast():
            left = 0
            right = len(nums) - 1
            res = -1

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    res = mid

                    # Search further right
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return res


        first = findFirst()

        if first == -1:
            return 0

        last = findLast()

        return last - first + 1
    