def minimum_length(nums: list[int], k: int) -> int:
    """nums contains only positive integers"""
    left = res = 0
    size = float('inf')
    
    for right in range(len(nums)):
        res += nums[right]
        
        # check res grater than k
        while left <= right and res >= k:
            size = min(size, right - left + 1)
            res -= nums[left]
            left += 1
        
    return size if size != float('inf') else -1
    
# k = int(input().strip())
# N = list(map(int, input().split()))4

N = [1,2,4,5,4,7]
k = 6
print(minimum_length(N, k))