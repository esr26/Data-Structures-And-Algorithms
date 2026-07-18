class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge_sort(nums):

            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            
            left, left_count = merge_sort(nums[:mid])
            right, right_count = merge_sort(nums[mid:])

            count = left_count + right_count

            j = 0

            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1

                count += j
             

            res = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                
                else:
                    res.append(right[j])
                    j += 1
            
            res.extend(left[i:])
            res.extend(right[j:])
            return res, count
        
        _, count = merge_sort(nums)
        return count


