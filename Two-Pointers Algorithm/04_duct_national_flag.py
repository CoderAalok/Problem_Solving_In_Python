from typing import List
def sortedArray(nums:List[int]) -> List[int]:
    low,mid = 0,0
    last = len(nums)-1
    
    # Initially at low, mid and last indices integer unknown
    while mid <= last:
        if nums[mid] == 0:
            #when it true then at 0 or low index  known integer 
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # skip
            mid += 1
        else:
            nums[mid],nums[last] = nums[last], nums[mid]
            last -= 1
    return nums

res = [0,1,2,0,2,1,0]
print(sortedArray(res))    