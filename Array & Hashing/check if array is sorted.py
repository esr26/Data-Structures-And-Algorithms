def isSorted(nums):

    n = len(nums)

    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            return False

    return True