class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        d = {0:0}
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            rem = curr_sum % k
            if rem in d:
                d[rem]+=1
                count += d[rem]
            else:
                d[rem]=0
        return count
            
