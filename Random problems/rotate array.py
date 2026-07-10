# def rotate(nums, k):
#     """We rotate the array to the right by k steps"""
    
#     n = len(nums)
#     k %= n # reduce k within range [0, n] and (k < n)
    
#     temp = nums[n-k : ] + nums[ : n-k]  # O(N)
    
#     for i in range(n):  # O(N)
#         nums[i] = temp[i]
    
#     return nums

# nums = [1,3,5,0,2,6]
# k = 3
# print(rotate(nums, k))

"""
Time Complexity: O(N)
Space Complexity: O(N)

"""

# Optimal approach (using constant space O(1))  (rotate + reverse)
""" Step by step what actually happening, while we can also compresed this logic into 'own' built-function called 'reverse' """

from typing import List
# def rotate(nums: List[int], k:int) -> List[int]:
#     n = len(nums)
#     k %= n # reduce k within range [0, n]
    
#     # reverse array
#     nums.reverse()
    
#     # reverse first k steps
#     i, j = 0, k-1
#     while i < j:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j -= 1
        
#     # reverse remaining elements
#     i, j = k, n-1
#     while i < j:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j -= 1
    
#     return nums

# Same logic just compressed version
def rotate(nums: List[int], k:int) -> List[int]:
    n = len(nums)
    k %= n # reduce k within range [0, n]
    
    # reverse array
    nums.reverse()
    
    def reverse(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
       
    # reverse first k steps
    reverse(0, k-1) 
    # reverse remaining elements
    reverse(k, n-1)
    # final result
    return nums

nums = [1,2,3,4,5,6]
k = 3
print(rotate(nums, k))


"""
DRY RUN:
# this reverse logic comes from my observation
# (right to left process happening, so this makes sense like reverse)
# overall, rotation + reverse = problem solved

nums.reverse() => [6,5,4,3,2,1], k = 3  
                   0 1 2 3 4 5

# reverse first k steps
i = 0, j = k-1 = 3-1 = 2 (True)
[4,5,6,3,2,1]
i = 1, j = 1 (False)

# reverse remaining elements
i = k = 3, j = n-1 = 6-1 = 5 (True)
[4,5,6,1,2,3]
i = 4, j = 4 (False)

final result:
nums = [4,5,6,1,2,3]

"""
"""
Time Complexity: O(N)
Space Complexity: O(1)

"""