from typing import List
def maxSumCircularSubarray(nums: List[int]) -> int:
    currmax = currmin = res = nums[0]
    totalSum = sum(nums)
    
    for i in range(1, len(nums)):
        currmax = max(nums[i], currmax + nums[i])
        currmin = min(nums[i], currmin + nums[i])
        res = max(res, currmax)

        if totalSum != currmin:
            res = max(res, totalSum - currmin)
        
    return res

# Output
nums = [3,4,-9,7]
print(maxSumCircularSubarray(nums))


""" 
******Working flow ******
-------------------------------------------
nums = [3,4,-9,7]

currmax = currmin = res = 3
totalSum = 5

i = 1
currmax = max(4, 3+4) = 7, [3, 4]
currmin = min(4, 3+4) = 4, [4] # start at i = 1

totalSum - currmin = 5 - 4 = 0
res = 7
----------------------------------------------------------------------

i = 2
currmax = max(-9, 7-9) = -2, [3, 4, -9]
currmin = min(-9, 4-9) = -9, [-9] # start at i = 2

totalSum - currmin = 5 - (-9) = 14
res = 14
----------------------------------------------------------------------

i = 3
currmax = max(-1, -2+7) = 5, [3,4,-9,7]
currmin = min(-1, -9+7) = -2, [-9, 7] 

totalSum - currmin = 5 - (-2) = 7
res = 14
----------------------------------------------------------------------

# # final result
res = 14, subarray = [3,4,7] 

"""