def secondSmallestLargest(nums):

    if len(nums) < 2:
        return -1

    first_max = max(nums)
    first_min = min(nums)

    second_max = float('-inf')
    second_min = float('inf')

    for num in nums:

        if first_max > num > second_max:
            second_max = num

        if first_min < num < second_min:
            second_min = num

    if second_max == float('-inf') or second_min == float('inf'):
        return -1

    return second_max, second_min