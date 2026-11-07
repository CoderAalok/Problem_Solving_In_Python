# def max_profit(nums: list[int]):
#     """Calculate the maximum profit/loss of two days"""
    
#     max_benifit = float('-inf')
#     i, j = 0, len(nums) - 1
#     pos_i, pos_j = i, j
    
#     while i < j:
#         _sum = nums[i] + nums[j] # two days profit
#         if _sum > max_benifit:
#             max_benifit = _sum
#             pos_i, pos_j = i, j

#         if nums[i] >= nums[j]:
#             j -= 1
            
#         else:
#             i += 1

#     return max_benifit, pos_i+1, pos_j+1


def maxSum(nums: list[int]):
    first = second = float('-inf')
    i1 = i2 = -1
    for i in range(len(nums)):
        if nums[i] > first:
            second, i2 = first, i1
            first, i1 = nums[i], i
            
        elif nums[i] > second:
            second, i2 = nums[i], i
        
    i1, i2 = (i1, i2) if i1 < i2 else (i2, i1)
    return (first + second, i1+1, i2+1)
    
print(maxSum([-2,9,3,9,1]))
    