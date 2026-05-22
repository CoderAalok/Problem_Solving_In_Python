def maxSubarraySum(nums):
    # nums =  [-3,1,4,5,-6]
            #  0,1,2,3,4,5
    # we find the best end, sum of all subarray whose ending index 'i'
    # for eg; i = 2; [-3,1,4], [1,4], [4]
    # continuous subarray or start new if greater than previous
    
    ans = end = nums[0]
    for i in range(1, len(nums)):
        add = nums[i] + end
        if add > nums[i]:
            end = add
            ans = max(ans, add)
        else:
            end = nums[i]
            ans = max(ans, nums[i])
    
    return ans

nums = [-3,1,4,5,-6]
print(maxSubarraySum(nums))
    