def missing_number(nums: list[int]):
    N = len(nums)
    sum_N = N * (N + 1) // 2
    
    seen = set()
    for n in nums:
        # find missing value and twice number
        if n in seen:
            missing_sum = sum(nums) - n  # n -> duplicate
            return (sum_N - missing_sum, n)
        seen.add(n)
        
    return 0

# Test:
nums = list(map(int, input('Integers: ').split()))
missing, duplicate = missing_number(nums)
print(f"Missing: {missing}")
print(f"Duplicate: {duplicate}")
