# # The problem of Sliding Window (Fixed window)
# # find maximum sum of subarray at size k.
# from typing import List
# def max_sum_subarray(nums:List[int], k:int) -> int:
#     if len(nums) < k or k <= 0:
#         return -1
    
#     left,right = 0,k-1
#     sum_ = res = 0
#     n = len(nums)
    
#     for s in range(k):  # O(n) 
#         sum_ += nums[s]
        
#     while right < n : # O(n)
#         # stored first result max
#         res = max(res,sum_)
#         # Increases both but size remain same
#         left += 1
#         right += 1
        
#         if right == n:
#             break
#         #shrink left
#         sum_ -= nums[left-1]
#         sum_ += nums[right] 
         
#     return res

# nums = [4,3,9,5,8]
# k = 2
# print(max_sum_subarray(nums, k))


# Revision
def max_Sum_subarray(nums, k):
    if not nums or len(nums) < k  or k <= 0:
        return -1
    
    low, high = 0, k-1
    k_sum, res = 0, float('-inf')
    n = len(nums)
    
    for s in range(k):
        k_sum += nums[s]
    
    while high < n:
        res = max(res, k_sum)
        # Now, find next k-size of subarray sum
        low += 1
        high += 1
        # check is high exceeding n 
        if high == n:
            break
        k_sum -= nums[low-1]
        k_sum += nums[high]
        
    return res

nums = [3,1,5,3,6,7]
k = 3
print(max_Sum_subarray(nums,k))  # -> 16