# from typing import List
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         low = count_zeros = res = 0
#         for high in range(len(nums)):
#             if nums[high] == 0:
#                 count_zeros += 1
#             while count_zeros > k:
#                 if nums[low] == 0:
#                     count_zeros -= 1
#                 low += 1
            
#             res = max(res, high-low+1)
    
#         return res
        
# s = Solution()
# nums= [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# print(s.longestOnes(nums,k))


from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = count_ones = res = 0
        for high in range(len(nums)):
            if nums[high] == 1:
                count_ones += 1
            while (high-low+1) - count_ones > k:
                if nums[low] == 1:
                    count_ones -= 1
                low += 1
            
            res = max(res, high-low+1)
    
        return res
    
s = Solution()
nums= [1,0,1]*1000000
k = 2
print(s.longestOnes(nums,k))