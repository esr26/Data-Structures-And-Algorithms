def merge_sort(nums):

    if len(nums) <= 1:
        return nums, 0

    mid = len(nums) // 2

    left, left_count = merge_sort(nums[:mid])
    right, right_count = merge_sort(nums[mid:])

    count = left_count + right_count

    i = 0
    j = 0
    res = []

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            res.append(left[i])
            i += 1

        else:
            # left[i] > right[j]
            # All elements from left[i:] are greater than right[j]
            count += len(left) - i

            res.append(right[j])
            j += 1

    # Add remaining elements
    res.extend(left[i:])
    res.extend(right[j:])

    return res, count


_, count = merge_sort(arr)
return count
