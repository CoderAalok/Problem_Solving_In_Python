"""
Problem: Sort the array elements even index -> even number and odd index -> odd number
"""

from typing import List
def sortEvenOdd(nums: List[int]) -> List[int]:
    even, odd = 0, 1
    while even < len(nums) and odd < len(nums):
        if nums[even] % 2 != 0 and nums[odd] % 2 == 0:
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2
            
        elif nums[even] % 2 == 0:
            even += 2
            
        elif nums[odd] % 2 != 0:
            odd += 2
    
    return nums
    
nums = [1,2,4,4,5]
print(sortEvenOdd(nums))

"""
Core Idea: At even index -> odd number and at odd index -> even number then swap it to become 
At even index -> even number and At odd index -> odd number"""

"""
DRY RUN:
nums = [1,2,4,4,5]
        0,1,2,3,4
        
even = 0, odd = 1
nums[even] -> odd num and nums[odd] -> even num 
swap: [2,1,4,4,5]

even = 2, odd = 3
nums[even] -> even num and nums[odd] -> even num 
even += 2

even = 4, odd = 3
nums[even] -> odd num and nums[odd] -> even num 
swap: [2,1,4,5,4]

Final result: [2,1,4,4,5]

"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""