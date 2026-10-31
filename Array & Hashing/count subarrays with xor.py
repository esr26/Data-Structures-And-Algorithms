def count_subarrays_with_xor(nums, k):
    prefix = {0: 1}
    curr = 0
    count = 0

    for num in nums:
        curr ^= num
        count += prefix.get(curr ^ k, 0)
        prefix[curr] = prefix.get(curr, 0) + 1

    return count
