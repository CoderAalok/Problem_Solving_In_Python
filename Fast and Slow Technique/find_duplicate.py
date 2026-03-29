# Brute force approach
# def find_duplicate(nums):
#     seen = set()
#     for n in nums:
#         if n in seen:
#             return n
#         seen.add(n)
        
# Second approach
from typing import List
# class Solution:
#     def findDuplicate(self, nums:List[int]) -> int:
#         slow = fast = nums[0] 
#         # step-1: cycle detection
#         while True:
#             # number as index  mapping it with to next number/element
#             slow = nums[slow] 
#             fast = nums[nums[fast]]
            
#             if slow == fast:
#                 # reset slow and keep holding fast at meeting point
#                 slow = nums[0]
#                 # now both move step by step
#                 while slow != fast:
#                     slow = nums[slow]
#                     fast = nums[fast]
                
#                 return slow

# s = Solution()
# print(s.findDuplicate(nums))
# Optimal approach
class Solution:
    def find_duplicate(self, nums:List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        # step-1: cycle detection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break        

        slow = nums[0]  #resetting 
        # step-2: entry point of cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # duplicate found
        return slow

s = Solution()
print(s.find_duplicate([1,2,3,4,3]))
