# def permutationInString(s1:str, s2:str) -> bool:
#     if not s1 or not s2 or len(s1) > len(s2):
#         return False
    
#     freq_s1 = [0]*26
#     freq_s2 = [0]*26
#     for i in range(len(s1)):
#         freq_s1[ord(s1[i]) - ord('a')] += 1
#         freq_s2[ord(s2[i]) - ord('a')] += 1
        
#     if freq_s2 == freq_s1:
#         return True
    
    
#     low = 0
#     for high in range(len(s1), len(s2)):
#         freq_s2[ord(s2[high]) - ord('a')] += 1
#         # shrinking
#         freq_s2[ord(s2[low]) - ord('a')] -= 1
#         low += 1
    
#         if freq_s2 == freq_s1:
#             return True
    
#     return False


# def permutationInString(s1:str, s2:str)->bool:
#     # edge case
#     n = len(s1)
#     m = len(s2)
#     if not s1 or not s2 or n > m:
#         return False
    
#     freq_s1 = [0]*26
#     for i in range(n):
#         char1 = s1[i]
#         freq_s1[ord(char1) - ord('a')] += 1
    
#     freq_s2 = [0]*26
#     low = 0
#     for high in range(m):
#         char2 = s2[high]
#         indx = ord(char2) - ord('a')
#         if freq_s1[indx]:
#             freq_s2[indx] += 1
#             while freq_s2[indx] > freq_s1[indx]:
#                 freq_s2[ord(s2[low]) - ord('a')] -= 1
#                 low += 1
                
#             if freq_s2 == freq_s1:
#                 return True
#         else:
#             freq_s2 = [0]*26
#             low = high+1
    
#     return False

# s1 = "abc"
# s2 = "cbqfbcccak"
# print(permutationInString(s1,s2))       
