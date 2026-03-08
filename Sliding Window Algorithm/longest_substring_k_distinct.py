# def longestSubstring(s:str, k:int)-> int:
#     low, res = 0, -1
#     hashmap = {}
    
#     for high,char in enumerate(s):
#         # stores character frequency
#         hashmap[char] = hashmap.get(char, 0) + 1
#         while len(hashmap) > k:
#             hashmap[s[low]] -= 1
#             if hashmap[s[low]] == 0:
#                 del hashmap[s[low]]
#             low += 1
        
#         if len(hashmap) == k:
#             size = high-low + 1
#             res = max(res, size)

#     return res

# s = 'aabacbebebe'
# k = 45
# print(longestSubstring(s,k))
