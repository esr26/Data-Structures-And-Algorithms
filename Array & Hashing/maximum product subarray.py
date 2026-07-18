class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suff = 1
        res = float('-inf')

        # Prefix product
        for num in nums:
            pre *= num
            res = max(res, pre)

            if pre == 0:
                pre = 1

        # Suffix product
        for i in range(len(nums) - 1, -1, -1):
            suff *= nums[i]
            res = max(res, suff)

            if suff == 0:
                suff = 1

        return res
        