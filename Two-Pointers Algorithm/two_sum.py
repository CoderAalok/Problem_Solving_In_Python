# Two sum (sorted array)
# return its index each incremented by one
def twoSum(nums, target):
    left, right = 0, len(nums)-1
    
    while left < right:
        total_sum = nums[left] + nums[right]
        if total_sum == target:
            return [left+1, right+1]
        elif total_sum > target:
            right -= 1
        else:
            left += 1
    

nums = [3,4,5,6,8]
target = 12
print(twoSum(nums, target))