class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        total_prod = 1
        
        for i in range(n): #O(n)
            total_prod *= nums[i] 

        prefix_sum = 0
        suffix_prod = total_prod
        for i in range(n): #O(n)
            suffix_prod //= nums[i]

            #check equality of sum and product
            if prefix_sum == suffix_prod:
                return i
            prefix_sum += nums[i]

        return -1
s = Solution()
arr = [4,2,3,1,6]
print(s.smallestBalancedIndex(arr))  
 # worst approach
        # for i in range(n):
        #     sum_left = sum(nums[ : i]) 
        #     prod_right = 1
        #     for p in nums[i+1: ]:
        #         prod_right *= p

        #     if sum_left == prod_right:
        #         return i

        # return -1

        # n = len(nums)
        # prefix_sum = [0]*(n+1) # starting sum considered as 0  # space: O(n+1) -> O(n)
        # surfix_prod = [1]*(n+1) # starting product considered as 1 # space: O(n+1)n -> O(n)

        # for s in range(n):
        #     prefix_sum[s+1] = prefix_sum[s] + nums[s]

        # for p in range(n-1, -1, -1):
        #     surfix_prod[p] = surfix_prod[p+1] * nums[p]

        # for i in range(n):
        #     if prefix_sum[i] == surfix_prod[i+1]:
        #         return i
                
        # return -1



        