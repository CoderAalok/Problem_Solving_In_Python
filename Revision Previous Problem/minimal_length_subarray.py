# def minimal_size_subarray(nums, target):  # only positive integer of target
#     if not nums or target <= 0:
#         return 0
    
#     low = 0
#     window_sum = 0
#     res = float('inf')
#     n = len(nums)
    
#     # while high < n:
#     for high in range(n):
#         window_sum += nums[high]
#         # checks Is window sum >= target
#         # until happening this the condition true
#         while window_sum >= target:
#             # find size of subarray
#             size = (high - low) + 1
#             # store current size
#             res = min(res, size)
#             # shrink low
#             window_sum -= nums[low]
#             # increment of low
#             low += 1
        
#         # next window
#         # high += 1
    
#     return 0 if res == float('inf') else res
    
# nums = [2,1,4,5,9]
# k = 90
# print(minimal_size_subarray(nums, k)) # -> 1
