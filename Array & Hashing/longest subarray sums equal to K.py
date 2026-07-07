def longestSubarray(nums, k):

    prefix = 0
    longest = 0

    mp = {0: -1}

    for i in range(len(nums)):

        prefix += nums[i]

        if prefix - k in mp:
            longest = max(longest, i - mp[prefix-k])

        if prefix not in mp:
            mp[prefix] = i

    return longest
