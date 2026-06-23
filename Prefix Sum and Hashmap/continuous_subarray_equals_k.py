from typing import List
def continuousSubarray(nums:List[int], k:int)-> int:
    # [23, 2, 4, 6, 7], 3
    
    seen = {0: -1} # Intialization
    subSum = 0
    
    for i in range(len(nums)):
        subSum += nums[i]
        rem = subSum % k
        
        if rem in seen:
            if i - seen[rem] >= 2:
                return (seen[rem], i)
        else:
            seen[rem] = i
            
    return -1

nums = [23, 2, 4, 6, 7]
k = 2
print(continuousSubarray(nums, k))


"""
Without initialization this algorithm only work for some input
It fail if only one possible subarray exist in array which reminder is 0.
"""

"""
Understand Mathematically,
[x1, x2, x3, x4, x5]

x1 % k = r1 ----(1)
(x1+x2) % k = r2
(x1+x2+x3) % k = r1  --- (2)

equation (2) - (1);
(x1+x2+x3) % k - x1 % k = r1- r1
(x2 + x3) % k = 0
# (x2 + x3) -> x
x % k == 0

"""

"""
Dry Run:

i = 0
subSum = 23
rem = 23 % 6 = 23 - 6(23//6) = 23 - 18 = 5


i = 1
subSum = 25
rem = 25 % k = 25 - 24 = 1

i = 2
subSum = 29
rem = 29 % 6 = 29 - 24 = 5

(29 - 23) % 6 = 5-5 = 0
6 % 6 = 0

result: True (0, 2)

"""