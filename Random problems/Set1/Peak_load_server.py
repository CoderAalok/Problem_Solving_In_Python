def peak_sum(nums: list[int]) -> int:
    n = len(nums) - 1
    i = 1 # exclude first element
    res = 0
    while i < n:  # exclude last element
        if nums[i-1] < nums[i] > nums[i+1]:
            res += nums[i]
            i += 2
        else:
            i += 1
        
    return res


N = int(input("N: ").strip())
nums = []
for _ in range(N):
    nums.append(int(input("Number: ").strip()))
    
print(peak_sum(nums))
    