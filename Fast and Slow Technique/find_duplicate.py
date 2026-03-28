# Brute force approach
# def find_duplicate(nums):
#     seen = set()
#     for n in nums:
#         if n in seen:
#             return n
#         seen.add(n)
        


# Optimal approach
from typing import List, Optional
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


# nums = [1,2,3,4,2]
# s = Solution()
# print(s.findDuplicate(nums))


# class Solution:
#     def find_duplicate(self, nums:List[int]) -> int:
#         slow = nums[0]
#         fast = nums[0]
#         # step-1: cycle detection
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break        

#         slow = nums[0]  #resetting 
#         # step-2: entry point of cycle
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[fast]
        
#         # duplicate found
#         return slow

# s = Solution()
# print(s.find_duplicate([1,2,3,4,3]))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]):
        n = ""
        slow = head
        while slow:
            n += str(slow.val)
            slow = slow.next
        
        n = int(n)
        x = n
        rem = 0
        while n != 0:
            rem = (rem*10) + (n % 10)
            n //= 10
        
        if rem == x:
            return True
        return False

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(1)

n1.next= n2
n2.next = n3
n3.next = n4

s = Solution()
print(s.isPalindrome(n1))
