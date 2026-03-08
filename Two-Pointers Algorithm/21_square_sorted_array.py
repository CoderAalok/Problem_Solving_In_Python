# from typing_extensions import List

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         neg = []
#         pos = []
#         res = []
#         i = j = 0 # i -> neg and j -> pos
        
#         # stored all positive or negative square
#         for x in nums:
#             if x < 0:
#                 neg.append(x*x)
#             else:
#                 pos.append(x*x)
        
#         neg.reverse()
#         n = len(neg)
#         m = len(pos)
#         # sorted them
#         while (i < n and j < m):
#             if neg[i] > pos[j]:
#                 res.append(pos[j])
#                 j += 1
#             elif neg[i] < pos[j]:
#                 res.append(neg[i])
#                 i += 1 
#             else:
#                 res.append(neg[i])
#                 res.append(pos[j])
                
#                 i += 1 
#                 j += 1
        
#         # if 'i' incompleted ( means last element)
#         while i < n:
#             res.append(neg[i])
#             i += 1

#          # if 'j' incompleted ( means last element)
#         while j < m:
#             res.append(pos[j])
#             j += 1
        
#         return res

# s = Solution()
# nums = [-4,-2,-1,0,1,3,4]
# print(s.sortedSquares(nums))



# Method-II (Time complexity: O(n) and Extra space: O(1))

def sortedSquares(nums):
    if not nums:
        return []
    
    n = len(nums)
    result = [0]*n #fixed result
    
    # # squaring all numbers
    for i,x in enumerate(nums):
        nums[i] = x*x
    
    left,right = 0,n-1 #for given input
    index = n-1 #for result
    
    while (left <= right):
        if nums[left] > nums[right]:
            # stored from right to left (means higher to lower)
            result[index] = nums[left]
            left += 1
        else:
            result[index] = nums[right]
            right -= 1
        
        index -= 1
    
    return result

            
nums = [-4,-2,-1,0,1,3,4]
print(sortedSquares(nums))
