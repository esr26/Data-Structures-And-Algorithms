def findKRotation(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum must be to the RIGHT of mid
            left = mid + 1
        else:
            # mid could itself be the minimum
            right = mid

    return left
