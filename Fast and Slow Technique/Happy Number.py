# class Solution:
#     def isHappy(self, n: int) -> bool:
#         ishappy = False
#         while not ishappy:
#             digits = [] # space used O(n)
#             while n != 0:
#                 rem = n%10
#                 n = n//10
#                 # store rem(digit)
#                 digits.append(rem)
            
#             res = 0
#             for d in digits:
#                 res += d**2
#             if res == 1:
#                 ishappy = True
#                 return ishappy
            
#             # reset
#             if res < 10:
#                 return False
#             n = res 
#             res = 0
#             digits = []
            
# s = Solution()
# print(s.isHappy(19))

# Optimized solution than previous solution
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set()
#         while n != 1:
#             if n in seen:
#                 return False
#             seen.add(n)
#             # extracting digits from -> n
#             res = 0
#             while n != 0:
#                 rem = n % 10
#                 n //= 10
#                 res += rem**2
#             n = res
#         return True
            
# s = Solution()
# print(s.isHappy(19))


# Great optimized solution
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         # Process recall
        
#         def get_next(n):
#             res = 0
#             while n != 0: #this loop depends on number -> n (n -> digits size -> (N) )
#                 d = n % 10 # each iteration -> digit reset 
#                 n //= 10
#                 res += d**2
#             return res
        
#         slow, fast = n, get_next(n) # fast pointer is initialized 1 step ahead then enter into cyclic loop
#         # does it is happy number or cyclic process
#         # this loop operation perform O(log(n))
#         while fast != 1 and slow != fast:  # (fast != 1 and slow == fast -> this confirm that a given number is not happy number)
#             slow = get_next(slow)
#             fast = get_next(get_next(fast))
#         return fast == 1
    
    

# # Time : O(log(n))
# # Space : O(1)
# s = Solution()
# print(s.isHappy(190))
