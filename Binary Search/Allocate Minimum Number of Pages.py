class Solution:
    def findPages(self, arr, m):

        if m > len(arr):
            return -1

        left = max(arr)
        right = sum(arr)

        while left <= right:

            mid = (left + right) // 2

            count = 1
            curr = arr[0]

            for num in arr[1:]:
                if curr + num <= mid:
                    curr += num
                else:
                    count += 1
                    curr = num

            if count <= m:
                right = mid - 1
            else:
                left = mid + 1

        return left

    