# def characterReplacement(s:str, k:int)-> int:
#     low = 0
#     res = -1 #float('-inf')
#     freq = [0]*26 #constant space
    
#     for high in range(len(s)):
#         # count frequency of character
#         freq[ord(s[high])-ord('A')] += 1
#         max_freq = max(freq)
#         # need changes exceed "k"
#         while (high-low+1) - max_freq > k:
#             # shrink low
#             freq[ord(s[low])-ord('A')] -= 1
#             low += 1
        
#         res = max(res, high-low+1)
    
#     return res 

# print(characterReplacement('ABBAAAB',2)) # -> 6


