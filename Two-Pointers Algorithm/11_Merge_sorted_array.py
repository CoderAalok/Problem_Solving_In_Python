# Brute force approach
# def merge(arr1,arr2,m,n):
#     for num in arr2:
#         arr1[m] = num
#         m += 1
#     # arr1.sort()
    
#     for i in range(len(arr1)):
#         for j in range(i+1, len(arr1)):
#             if arr1[i] >= arr1[j]:
#                 arr1[i],arr1[j] = arr1[j],arr1[i]
    
#     return arr1
    

# Optimal solution

from typing import List
def merge(arr1:List[int], arr2:List[int], m:int, n:int) -> List[int]:
    i, j = m-1, n-1
    k = (m+n)-1
    
    while (j >= 0):
        if i>= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    
    return arr1

print(merge([1,2,3,8,9],[3,5], 3,2))