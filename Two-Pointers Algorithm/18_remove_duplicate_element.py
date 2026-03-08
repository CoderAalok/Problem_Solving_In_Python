# modified an array the unique nums must apprears, what beyond leaves does not matter

# Method-I (Using two pointer)
# def remove_duplicate(nums):
#     if not nums:
#         return []
    
#     i = 0
#     j = k = 1 
#     while j< len(nums):
#         if nums[j] != nums[j-1]:
#             nums[i+1] = nums[j]
#             k+= 1
#             i +=1
#         j+=1
#     return k,nums
# n = [1,1,1,1,1,1,2,2,3]
# print(remove_duplicate(n))

# Method-II
# def remove_duplicate(nums):
#     k = 1 # ensure first number must be unique
#     n = len(nums)-1
    
#     for x in range(1,n):
#         if nums[x] != nums[k-1]:
#             nums[k] = nums[x]
#             k +=1 
#     return k, nums

# n = [1,1,1,1,1,1,2,2,3]
# print(remove_duplicate(n))

# modified an array atmost twice nums apprears

def removeDuplicate(nums):
    if not nums:
        return 0
    
    k = 0 # fixed twice unique appeared
    
    for i in nums:
        if k < 2 or i != nums[k-2]:
            nums[k] = i
            k += 1
        
    return k, nums

n = [0,0,0,1,1,1,2,2,3]
print(removeDuplicate(n))