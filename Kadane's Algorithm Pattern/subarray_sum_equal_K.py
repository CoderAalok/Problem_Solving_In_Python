from typing import List
def subarraySum(nums: List[int], k:int) -> int:
    # nums = [1,2,1,2,1], prefixSum = [0,1,3,4,6]
    
    freqSum = {0:1} # Inilitillize prefix sum frequency 1 at i = 0
    prefSum = count = 0  # prefix sum at i = 0 is 0 and result count
    
    for i in range(len(nums)):
        prefSum += nums[i] # sum(0,...,i)
        
        # (prefSum - k) -> a value whose sum equals to subarray(0,...,i)
        # this make ensure that total prefix sum - returned value exactly equals to 'k'.
        count += freqSum.get((prefSum - k), 0)
        
        # history and avoid re-scaning
        freqSum[prefSum] = freqSum.get(prefSum, 0) + 1
    
    return count

# test
# nums = [1,2,1,2,1]
# k = 3
nums = [1,-1,0]
k = 0
print(subarraySum(nums, k))


                        # Dry Run
"""
                        # nums = [1,-1,0]
                        Index:    0, 1,2
                        --------------------------
                        freqSum = {0:1} # prefSum == k, (i.e. (prefSum - k) = 0), so therefore subarray sum(0,..,i) -> prefSum exactly equals to 'k'.
                        prefSum = 0 # at i = 0

                        i = 0
                        prefSum = 0 + 1
                        prefSum - k = 1 - 0 = 1
                        count = 0
                        freqSum = {0:1, 1:1}

                        i = 1
                        prefSum = 1 + (-1) = 0
                        prefSum - k = 0 - 0 = 0
                        count = 0 + 1
                        freqSum = {0:2, 1:1}

                        i = 2
                        prefSum = 0 + 0
                        prefSum - k = 0 - 0 = 0
                        count = 1 + 2 = 3
                        freqSum = {0:3, 1:1}

                        # final result
                        count = 3 # subarray: [1,-1] [1,-1,0], and [0]

"""