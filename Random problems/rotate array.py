def rotate(nums, k):
    n = len(nums)
    k %= n # reduce k within range [0, n] and (k < n)
    
    temp = nums[n-k : ] + nums[ : n-k]
    
    for i in range(n):
        nums[i] = temp[i]
    
    return nums

nums = [1,3,5,0,2,6]
k = 3
print(rotate(nums, k))