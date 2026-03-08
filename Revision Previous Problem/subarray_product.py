from typing import List
def subarray_product(nums:List[int], target:int)-> int :
    if target <= 1:
        return 0
    
    low = count = 0
    prod = 1
    
    for high in range(len(nums)):
        
        prod *= nums[high]
        
        while prod >= target:
            prod //= nums[low]
            low += 1

        count += high-low+1

    return count

res = [1,2,0,4]
target = 20
print(subarray_product(res,target))  # -> 8