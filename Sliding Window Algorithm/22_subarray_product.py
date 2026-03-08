# # only for positive array 
# def productSubarray(nums, target): #result: int
#     # avoid <= 1 value of target of this problem
#     if target <= 1:
#         return 0
    
#     low = 0
#     num_subarray = 0
#     prod = 1
#     n = len(nums)
    
#     for high in range(n):
#         prod *= nums[high]
#         # check condition
#         while prod >= target :
#             # shrink low
#             prod //= nums[low]
#             low += 1
#         # count all valid contiguous subarray 
#         num_subarray += high-low+1
    
#     return num_subarray

# nums = [2,1,4,9]
# k = 50
# print(productSubarray(nums,k)) #-> 6+3=9
    

def smallest_size_product_subarray(nums, target):
    if target <= 1:
        return 0
    
    low = 0
    res = float('inf')
    n = len(nums)
    prod = 1
    
    for high in range(n):
        prod *= nums[high]
        while prod >= target:
            size = high-low+1
            res = min(res, size)
            prod /= nums[low]
            low += 1
        
    return 0 if res == float('inf') else res 

nums = [2,3,10,12]
k = 1000
print(smallest_size_product_subarray(nums,k))