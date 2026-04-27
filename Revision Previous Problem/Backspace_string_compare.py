# class Solution:
#     def backspaceCompare(self, s1:str, s2:str) -> bool:
#         # edge case
#         if not s1 or not s2:
#             return False
            
#         # Using backward traverse logic
#         # 
#         # def backspaceSimulation(string):
#         #     typed = ""
#         #     skip = 0
#         #     n = len(string)
#         #     i = n - 1
            
#         #     while i <= 0:
#         #         if string[i] == '#':
#         #             skip += 1
                
#         #         elif skip > 0:
#         #             skip -= 1
                
#         #         else:
#         #             typed += string[i]
                
#         #     return typed[:: -1]
    
#         # return backspaceSimulation(s1) == backspaceSimulation(s2)
        
        
#         # Using stack simulation
#         def stackSimulation(string):
#             stack = []
#             for ch in string:
#                 if ch == "#":
#                     if stack:
#                         stack.pop(-1)
#                 else:
#                     stack.append(ch)
            
#             # return stack
#             # OR
#             return "".join(stack)
        
#         return stackSimulation(s1) == stackSimulation(s2)


# s = Solution()
# s1 = "abc#"
# s2 = "#"
# print(s.backspaceCompare(s1, s2))
