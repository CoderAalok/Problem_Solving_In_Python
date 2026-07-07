def countNiceSubarray(nums, k) -> int:
    # edge case
    N = len(nums)
    if N < k:
        return 0
    
    # replacing even with 0 and odd with 1
    for i in range(N):
        nums[i] = 1 if nums[i] % 2 != 0 else 0
    
    prefSum = 0 # initialize at i = 0
    seen = {0 : 1} # {prefSum : frequency}
    res = 0
    
    for i in range(N):
        prefSum += nums[i]
        prevPref = prefSum - k  # prefixSum[i] - k = prefixSum[j]
        res += seen.get(prevPref, 0)
        seen[prefSum] = seen.get(prefSum, 0) + 1
        
    return res
        

# nums = [2,3,1,5]
nums = [2,2,2,1,2,2,1,2,2]
k = 2
print(countNiceSubarray(nums, k))


"""" Subarray Sum of frequency of odd (x) exactly equals to k (i.e. x == k) """
# DRY RUN
"""
first a fall, replacing even with 0 and odd with 1
i.e. nums = [0,1,1,1] , k = 3

prefSum = 0
seen = {0 : 1}  # how many times 0 prefSum seen obviously 1 time 
res = 0

i = 0
prefSum = 0
res = 0
seen = {0:2}

i = 1
prefSum = 1
res = 0
seen = {0:2, 1:1}

i = 2
prefSum = 1
res = 0
seen = {0:2, 1:1}

i = 2
prefSum = 2
res = 0
seen = {0:2, 1:1, 2:1}

i = 3
prefSum = 3
res = 2
seen = {0:2, 1:1, 2:1, 3:1}

# final result:
Number of nice sub-array  which contains k odd numbers on it = 2 #[2,1,3,5] and [1,3,5]

"""

"""
Time Complexity: O(n) [Becasue N times operation perform]
Space Complexity: O(n) [Because we use here hashmap]

:: Linear time and linear space
"""