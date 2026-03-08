# Time complexity: O(n), Because in this problem backward process is not happening (means: reversed process, staright forward process).
# low increases in some condition only, high increases in each iteration.

# Space: O(1)

def minimalSizeSubarray(arr, target):
    low = high = 0
    sum_ = 0
    n = len(arr)
    res = float('inf')
    
    while high < n:
        sum_ += arr[high]
        # shrink
        while sum_ >= target:
            size = (high - low) + 1
            res = min(res, size)
            sum_ -= arr[low]
            low += 1
        # new window
        high += 1
    
    return 0 if res == float('inf') else res

nums = [12,28,83,4,25,26,25,4,25,25,25,12]
target = 213
print(minimalSizeSubarray(nums, target)) # 8
