def third_largest(nums: List[int]) -> int:
    if  len(nums) < 3:
        return -1
    
    first_last = second_last = third_last = float('-inf')
    
    for num in nums:
        if num > first_last:
            third_last = second_last
            second_last = first_last
            first_last = num
            
        elif num > second_last:
            third_last = second_last
            second_last = num
    
        elif num < first_last and num < second_last and num > third_last:
            third_last = num
        
    return -1 if third_last == float('-inf') else third_last

# test
nums = [2,1,5,3,9]
print(third_largest(nums))

"""
Time Complexity: O(n)
Space Compexity: O(1)

"""
