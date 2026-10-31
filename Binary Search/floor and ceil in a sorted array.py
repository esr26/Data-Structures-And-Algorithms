def floor_and_ceil(nums, target):
    left = 0
    right = len(nums) - 1
    floor = -1
    ceil = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        if nums[mid] < target:
            floor = nums[mid]
            left = mid + 1
        else:
            ceil = nums[mid]
            right = mid - 1

    return [floor, ceil]
