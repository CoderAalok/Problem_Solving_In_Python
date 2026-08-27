from typing import List
def moves_zeros(nums: List[int]) -> List[int]:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            
    return nums

# test case
nums = [0,0,1,0,0,2]
print(moves_zeros(nums))


""" 
Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Core logic: All zeros shift to the end and reset of non-zero element in there relative order.
Overall, thing is if at i = 0, element = 0 then we stay at that index and we're moving forward looking for non-zero element that we switch/swap to it.
So, same thing apply next index also.

"""

"""
nums = [0,0,1,0,0,2]
left = 0, right = 0
0 != 0 (False)
left = 0, right = 1
0 != 0 (False)

left = 0, right = 2
1 != 0 (True)
swap -> left-right and right-left
nums = [1,0,0,0,0,2]

left = 1, right = 3
0 != 0 (False)
left = 1, right = 4
0 != 0 (False)

left = 1, right = 5
again swap -> left-right and right-left
nums = [1,2,0,0,0,0]

# Final result:
nums = [1,2,0,0,0,0]
"""