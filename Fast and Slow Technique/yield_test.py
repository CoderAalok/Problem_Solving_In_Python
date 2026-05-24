def cumSum(nums):
    cum_sum = 0
    for i in range(len(nums)):
        cum_sum += nums[i]
        nums[i] = cum_sum
    yield nums
print(next(cumSum([9,2,3,4,5])))

