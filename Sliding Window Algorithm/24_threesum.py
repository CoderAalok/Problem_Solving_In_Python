# ThreeSum problem solve as like twoSum problem
# The sum of three numbers is equal to zero.
# a+b+c = 0 a = -(c+b) (In a Programming context)

# without using two pointer
# 1: creates a hashset()
# 2: first for loop (i) inside it has another set() as two store number's' complement
# 3: second for loop (j) 
# 4: find complement of j index element then 
# 5: check in seen if true
# 6: store in tuple format with sorted
# (because prevent the duplicate values,
# so this done each treplet stored in sorted format which helps to prevent duplicate value.) 
# (nums[i],nums[j],complement) in treplet set
# 7: if false then keep store j index element.
# 8: lastly, before return set of tuple into list of list
# According to this problem the triplets has any order.

# Method-I
# def threeSum(nums):
#     nums.sort() #
#     triplets = set() #all non-duplicate triplets values
    
#     for i in range(len(nums)): #start to fix i at 0 and vary after completion inner loop 
#         if i > 0 and nums[i] == nums[i-1]: #avoid the unnecessary work means not work for any duplicates elements
#             continue 
        
#         seen = set() #reset each iteration
        
#         for j in range(i+1, len(nums)):
#             complement = -(nums[j] + nums[i])
#             if complement in seen:
#                 triplets.add(tuple(sorted([nums[i],nums[j],complement])))
                
#             # when the complement of  nums[j] is not match
#             else:
#                 # nums[j] element stored
#                 seen.add(nums[j])

#     return [list(t) for t in triplets] #set of tuple to list of list


# Method-II
# nums = [-1,0,1,2,-1,-4]
# nums = [0]*10000
# print(threeSum(nums)) 

# # # Too small input
# def threeSum(nums):
#         count_triple = [[nums[i], nums[j], nums[k]] 
#                 for i in range(len(nums))
#                 for j in range(i+1, len(nums))  
#                 for k in range(j+1, len(nums))
#                 if (nums[i] + nums[j] + nums[k] == 0)
#         ]

#         triple = []
#         for t in count_triple:
#             t = sorted(t)
#             if t not in triple:
#                   triple.append(t)
        
#         return (triple)

# r = threeSum([-1,0,1,2,-1,3,4,0,8,-9,6])
# print(r)


# Method-III  (Time Complexity: O(n^2))
from typing import List
def threeSum(nums:List[int], target:int) -> List[List[int]]:
    nums.sort() #O(n.log n)
    n = len(nums)
    triplet = []
    i = 0
    
    while i < n-2: #O(n)
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue  #if seen any previous nums same as current then skip it
        
        j = i+1  #O(n)
        k = n-1  #O(n)
        while j<k: #O(n)
            
            total = nums[i]+nums[j]+nums[k]
            if total == target:
                triplet.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
        
            elif total > target:
                k -= 1
                
            elif total < target:
                j += 1
                
            while k>j and nums[k] == nums[k+1]:
                k -= 1
                continue
            while j<k and nums[j] == nums[j-1]:
                j += 1
                continue
        i += 1
        
    return triplet

res = threeSum([-1,0,1,2,-1,-1],0)
print(res)

# Brute force algorithm
# def threeSum(nums):
#     nums.sort()
#     res = []
#     seen = set()
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1):
#                 sum = nums[i]+nums[j]+nums[k]
#                 if sum == 0:
#                     s = tuple(sorted([nums[i],nums[j],nums[k]]))
#                     if s not in seen:
#                         seen.add(s)
#                         res.append(s)
#     return [list(r) for r in res]

# res = threeSum([-1,0,1,2,-1,-1])
# print(res)
                
            
        
           
             