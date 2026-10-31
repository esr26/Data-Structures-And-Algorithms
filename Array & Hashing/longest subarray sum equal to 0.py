def longest_zero_sum_subarray(nums):
    prefix = 0
    first_seen = {0: -1}
    longest = 0

    for i, value in enumerate(nums):
        prefix += value
        if prefix in first_seen:
            longest = max(longest, i - first_seen[prefix])
        else:
            first_seen[prefix] = i

    return longest
