prefix = {0: 1}
curr = 0
count = 0

for num in nums:

    curr ^= num          # XOR, not addition

    if (curr ^ k) in prefix:
        count += prefix[curr ^ k]

    prefix[curr] = prefix.get(curr, 0) + 1

return count