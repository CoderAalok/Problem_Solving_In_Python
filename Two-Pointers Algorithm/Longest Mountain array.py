from typing import List
def longestMountain(arr:List[int]) -> int:
    N = len(arr)
    start = longest = 0
    if N < 3:
        return longest
    
    while start < N:
        end = start
        
        if end + 1 < N and arr[end] < arr[end+1]:
            # climb up: at the end of this loop we reached at peck point
            while end + 1 < N and arr[end] < arr[end+1]:
                end += 1
            
            # peak = end
            if end + 1 < N and arr[end] > arr[end+1]:
                # climb down: at the of this loop we reached at bottom/valley point
                while end + 1 < N and arr[end] > arr[end+1]:
                    end += 1
                
                    # calculate length at each end of subarray
                    longest = max(longest, end-start+1)
        
        # update start
        start = max(end, start+1)
        
    # final result: longest mountain subarray
    return longest

# arr = [2,1,0,2,4,7,5,2,10]
arr = [1,0,7,3,1,6]
print(longestMountain(arr))


"""
arr = [1,0,5,3,1,6]
       0 1 2 3 4 5
N = 6

# Visualization:
   6 |        peak        /
   5 |         /\        /
   4 |        /  \      /
   3 |       /    \    /
   2 |      /      \  /
   1 |  \  /        \/
   0 |___\/_________end__________
       start/base
"""


"""
# DRY RUN:
start = 0, end = start, longest = 0
_______________________________________________________________________

0+1 < 6 and 1 < 0 (False)
# update start point
start = max(end, start+1) = max(0, 0+1) = 1
_______________________________________________________________________

start = 1, end = start, longest = 0
1+1 < 6 and 0 < 5 (True)
fisrt Loop run: climb up
end = 2 -> (peak)
2+1 < 6 and 5 < 3 (False)
_______________________________________________________________________

second Loop run: climb down
2+1 < 6 and 5 > 3 (True)
end = 3
longest = max(longest, end-start+1) = max(0, 3-1+1) = 3
3+1 < 6 and 3 > 1 (True)
end = 4
longest = max(longest, end-start+1) = max(0, 4-1+1) = 4
4+1 < 6 and 1 > 6 (False)
_______________________________________________________________________

# update start point
start = max(end, start+1) = max(4, 1+1) = 4
_______________________________________________________________________

# Final result:
Longest Mountain subarray = 4 (i.e. [0,5,3,1])

"""

""" 
# Mainly we update start as like  this (start = end)

but this only if starts with both left boundary and right boundray   (/\/\)
    
In some cases, mountain starts with right boundary like  (\/\/\)
    
so, handling these both cases efficient using this (start = max(end, start+1))

"""