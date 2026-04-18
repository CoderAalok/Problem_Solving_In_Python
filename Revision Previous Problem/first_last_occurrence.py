from typing import List
class Solution:
    def first_last_occurrence(self, nums:List[int], target:int) -> List[int]:
        # edge case
        if not nums:
            return [-1, -1]
        
        # length of array
        n = len(nums)
        
        # first occurrence
        left, right = 0, n-1
        first_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_index = mid
                # eliminate half and continue searching to find boundary of first
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # mid-value exceed target value, eliminate right half
                right = mid - 1
            
        # last occurrence
        left, right = 0, n-1
        last_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_index = mid
                # eliminate half and continue searching to find boundary of last
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # mid-value exceed target value, eliminate rigth half
                right = mid - 1
        
        # result
        return [first_index, last_index]
        
nums = [1,2,2,2,3,3,4]
nums = []
target = 2
s = Solution()
print(s.first_last_occurrence(nums, target))