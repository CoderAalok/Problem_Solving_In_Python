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
    