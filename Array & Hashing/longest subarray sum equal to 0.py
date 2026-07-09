prefix = 0
mp = {0: -1}

longest = 0

for i in range(len(nums)):

    prefix += nums[i]

    if prefix in mp:
        longest = max(longest, i - mp[prefix])

    if prefix not in mp:
        mp[prefix] = i

return longest