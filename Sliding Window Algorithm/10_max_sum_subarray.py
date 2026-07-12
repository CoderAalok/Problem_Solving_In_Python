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
    
    n = len(nums)
    window_sum = max_sum = 0 
    left, right = 0, k-1
    
    for i in range(k):
        window_sum += nums[i]
    
    for right in range(k, n):
        window_sum += nums[right] - nums[right - k]
        max_sum = max(max_sum, window_sum)
        
    # while right < n:
    #     max_sum = max(max_sum, window_sum)
    #     left += 1
    #     right += 1
    #     if right == n:
    #         break
        
    #     window_sum += nums[right] - nums[left-1]
    
    return max_sum
    
    
nums = [3,1,5,3,6,7]
k = 3
print(max_Sum_subarray(nums, k))  # -> 16