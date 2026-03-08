# class Solution:
#     def countTriplets(self, n, sum, arr):
#         #code here
#         arr.sort()
#         count = 0 #count of triplets whose sum less than sum(target)
#         for low in range(n):
#             mid,high = low+1, n-1
            
#             while (low<mid < high):
#                 total_sum = arr[low]+arr[mid]+arr[high]
#                 if total_sum >= sum:
#                     high -= 1
#                 else:
#                     count += (high-mid)
#                     mid += 1
              
#         return count
    
# s = Solution()
# print(s.countTriplets(5, 86,[30, 8 ,23, 6, 10]))


from typing import List
def tripletsmallersum(arr:List[int], target:int) -> int:
    if len(arr) < 3 or target < 0:
        return -1
    
    arr.sort()
    count = 0
    n = len(arr)
    for low in range(n-2):
        mid, high = low+1, n-1
        while mid < high :
            total_sum = arr[low]+arr[mid]+arr[high]
            if total_sum >= target:
                high -= 1
            else:
                count = count + (high - mid)
                mid += 1
    return count

# res = tripletsmallersum([4,1,0,2,3,-1,3,5],10)
# print(5+4+3+2+1+5+4+3+2+1+4+3+2+1+3+2+1+1+1)
# print(res) # res: 5+4+3+2+1+5+4+3+2+1+4+3+2+1+3+2+1+1+1 = 48

res = tripletsmallersum([4,1,0,2],10)
print(res) #res -> 4
