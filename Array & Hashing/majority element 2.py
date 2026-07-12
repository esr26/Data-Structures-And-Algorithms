class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1 = 0
        count2 = 0
        res = []

        cand1 = cand2 = None

        for num in nums:

            if num == cand1:
                count1 += 1
            
            elif num == cand2:
                count2 += 1

            elif count1 == 0:
                cand1 = num
                count1 = 1
            
            elif count2 == 0:
                cand2 = num
                count2 = 1
            
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0

        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1

        threshold = len(nums)//3

        if count1 > threshold:
            res.append(cand1)

        if count2 > threshold:
            res.append(cand2)
        
        return res
