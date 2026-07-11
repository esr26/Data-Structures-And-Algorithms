max_value = float('-inf')
res = []

for i in range(len(nums)-1, -1, -1):
    if nums[i] > max_value:
        res.append(nums[i])
        max_value = nums[i]

left = 0
right = len(res)-1
while left < right:
    res[left], res[right] = res[right], res[left]
    left += 1
    right -= 1

return res