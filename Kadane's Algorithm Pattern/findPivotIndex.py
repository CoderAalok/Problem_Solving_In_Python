# Pivot index means sum of all numbers strictly to the left equals to sum of all numbers strictly to the right
# left sum -> prefix sum and right sum -> suffix sum

from typing import List
def pivotIndex(nums:List[int])-> int:
    # nums = [1,7,3,6,5,6]
    leftSum = 0
    totalSum = sum(nums)
    
    for i in range(len(nums)):
        rightSum = totalSum - leftSum - nums[i]
        if leftSum == rightSum:
            return i
    
        leftSum += nums[i]
        
    return -1
    
# test
# nums = [1,7,3,6,5,6] 
# print(pivotIndex(nums))





                                    # Core Intuition
"""
                                    nums = [1,7,3,6,5,6], totalSum = 28
                                    index:  0,1,2,3,4,5

                                    leftSum = [0,1,8,11,18,23]  # Note: at 0th index no any prefix(left) sum (i.e. 0)
                                    index:     0,1,2,3, 4,  5  

                                    rightSum = [27,20,17,11,6,0] # Note: at 0th index no any suffix(right) sum (i.e. 0)
                                    index:      0, 1, 2, 3, 4,5  
"""

                                    # Dry run
"""
                                    nums = [1,7,3,6,5,6], totalSum = 28
                                    leftSum = 0

                                    i = 0
                                    rightSum = 28 - 0 - 1 = 27

                                    i = 1
                                    rightSum = 28 - 1 - 7 = 20

                                    i = 2
                                    rightSum = 28 - 8 - 3 = 17

                                    i = 3
                                    rightSum = 28 - 11 - 6 = 11

                                    # result
                                    pivot index = 3

"""