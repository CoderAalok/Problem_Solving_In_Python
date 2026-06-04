from typing import List
def maximumProduct(nums: List[int]) -> int:
    # nums = [-5,3,9,-2,-7]
    """ 
    ***** Two possible cases *****
    -----------------------------------------------------------------
    Case 1: Positive largest * Positive largest = maximum prodcut
    Case 2: Negative smallest * Negative smallest = maximum product
    
    """
    currMax = currMin = res = nums[0]
    for i in range(1, len(nums)):
        # calculate maximum product
        maxProd = currMax * nums[i]
        # calculate minimum product
        minProd = currMin * nums[i]
        # currMax and curMin updates
        currMax = max(nums[i], maxProd, minProd)
        currMin = min(nums[i], maxProd, minProd)
        
        # update result
        res = max(res, currMax)
    
    return res


nums = [-5,3,9,-2,-7]
print(maximumProduct(nums))



"""
                                                    *********** Working flow ************
                                                    -----------------------------------------------
                                                    nums = [-5, 3, 9, -2, -7]
                                                    currMax = curMin = res = -5 # at i = 0 only one possible subarray (so, the best ending at 0 index which is -5)
                                                    
                                                    i = 1
                                                    currMax = max(3, -15, -15) -> 3, [3]
                                                    currMin = min(3, -15, -15) -> -15, [-5, 3]
                                                    res = 3
                                                    
                                                    i = 2
                                                    currMax = max(9, 27, -135) -> 27, [3, 9]
                                                    currMin = min(9, 27, -135) -> -135, [-5, 3, 9]
                                                    res = 27
                                                    
                                                    i = 3
                                                    currMax = max(-2, -54, 270) -> 270, [-5, 3, 9, -2]
                                                    currMin = min(-2, -54, 270) -> -54, [3, 9, -2]
                                                    res = 270
                                                    
                                                    i = 4
                                                    currMax = max(-7, 378, -1890) -> 378, [3, 9, -2, -7]
                                                    currMin = min(-7, 378, -1890) -> -1890, [-5, 3, 9, -2, -7]
                                                    res = 378
                                                    
                                                    # final result
                                                    res = 378, subarray = [3, 9, -2, -7]
                                                    
                                                    
"""