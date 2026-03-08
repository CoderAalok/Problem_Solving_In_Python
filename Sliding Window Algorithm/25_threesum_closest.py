from typing import List
def threeSumClosest(nums:List[int], target:int) -> int:
    nums.sort()
    max_diff = float('inf')
    res = -1 #initially assumed as default result 
    n = len(nums)
    
    for i in range(n-2):
        j,k = i+1, n-1
        
        while (j<k):
            total_sum = nums[i]+nums[j]+nums[k]
            diff = abs(total_sum-target)
            if diff < max_diff:
                max_diff = diff
                res = total_sum
            
            if total_sum == target:
                return res
            elif total_sum > target:
                k -= 1
            else:
                j += 1
    
    return res

res = [2,-4,-5,1,0,-2] # after sort -> [-5,-4,-2,0,1,2]
print(threeSumClosest(res, 5))
