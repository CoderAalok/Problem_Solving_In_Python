# find twosum index by using fundamental maths concept (a+b = c).
# firstly, keep on mind in this problem we used hashmap.
# First we store each number's of its complement' as key and it's value as index.
# After then find complement and check this complement on hashmap, If match return indices. 

# Method-I
# def twoSum(nums, target):
#     if len(nums) < 2:
#         return None
    
#     hashmap = {}
#     for i, b in enumerate(nums):
#         complement = target - b  #a+b = c
#         if complement in hashmap:
#             return (hashmap[complement], i)
#         else:
#             hashmap[b] = i

# nums = [4,9,-1,3,5,10]
# k = 19
# print(twoSum(nums, k))

# Method-II
# def twoSum(nums, target):
#     if len(nums) < 2:
#         return None
#     hashmap = {}
#     for i in range(len(nums)):
#         hashmap[target - nums[i]] = i
    
#     for a in range(len(nums)):
#         if nums[a] in hashmap:
#             if (nums[a] + nums[hashmap[nums[a]]]) == target:
#                 return (a, hashmap[nums[a]])        
#     return []            
# nums = [-1,3,5,10]
# k = 6
# print(twoSum(nums, k))


# Method-III 
# (Two pointer-I)-> (This solution only for sorted array work)
# def two_sum(arr, target):
#     low = 0
#     high = len(arr)-1
#     while (low<high):
#         total = arr[low]+arr[high]
        
#         if total == target:
#             return (low, high)
#         elif total < target:
#             low += 1
#         else:
#             high -= 1
            
# arr = [2,3,4,5]
# t = 6
# print(two_sum(arr,t))


# Two-sum -> return numbers
def twoSum(nums, target):
    dic = {}
    for a in nums:
        complement = target - a
        if complement in dic:
            return [complement, a]
        else:
            dic[a] = complement
            
res = twoSum([2,3,4,5],9)            
print(res)
