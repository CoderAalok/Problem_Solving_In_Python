def findShortestSubarray(nums) -> int:
    # Edge case
    if not nums or len(nums) < 2:
        return 0
    
    start = end = 0
    max_left = nums[0]
    min_right = nums[-1]
    
    # First travers: left-right -> find unsorted end index
    for i in range(len(nums)):
        if nums[i] >= max_left:
            max_left = nums[i]
        else:
            end = i
    
    # Second travers: right-left -> find unsorted first index
    for j in range(len(nums)-1, -1, -1):
        if nums[j] <= min_right:
            min_right = nums[j]
        else:
            start = j
    
    # check Is already sorted
    if end == 0:
        return 0
    
    # result
    return end - start + 1

nums = [2,6,1,3,8,10,9,20]
print(findShortestSubarray(nums))
