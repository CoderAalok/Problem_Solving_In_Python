# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_nums = {
#             "M": 1000,
#             "D": 500,
#             "C": 100,
#             "L":  50,
#             "X": 10,
#             "V": 5,
#             "I": 1
#         }

#         prev = 0
#         ans = 0
#         for i in range(len(s)):
#             curr = roman_nums[s[i]]
#             if curr > prev:
#                 ans  = ans - 2 * prev + curr
#             else:
#                 ans += curr
            
#             prev = curr

#         return ans
        
# s = Solution()
# print(s.romanToInt('MMCDX'))  