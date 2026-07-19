left = 0
right = len(nums) - 1

floor = -1
ceil = -1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        return [nums[mid], nums[mid]]

    elif nums[mid] < target:
        # Possible floor
        floor = nums[mid]

        # Search for a larger floor
        left = mid + 1

    else:
        # Possible ceil
        ceil = nums[mid]

        # Search for a smaller ceil
        right = mid - 1

return [floor, ceil]
