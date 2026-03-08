# # def findAnagram(s,p):
# #     word_p = [0]*26 # space: O(1)
# #     anagram = {}
# #     n = len(p)
# #     for c in range(n):
# #         word_p[ord(p[c]) - ord('a')] += 1
    
# #     key = tuple(word_p)
# #     anagram[key] = [] #space: O(1)  # key -> constant that a key
    
# #     low = 0
# #     word_s = [0]*26 #space: O(1)
# #     for high in range(len(s)):
# #         word_s[ord(s[high]) - ord('a')] += 1
# #         while (high-low+1) > n:
# #             word_s[ord(s[low]) - ord('a')] -=1
# #             low += 1
    
# #         word = tuple(word_p) 
# #         if (high-low+1) == n and word in anagram:
# #             anagram[word].append(low)

# #     return list(anagram.values())[-1]

# # # Time: O(n)
# # # Space: O(1)

# # print(findAnagram('abab','ab'))


# def findAnagram(s,p):
#     n = len(p)
#     freq_p = [0]*26 # space: O(1)
#     for c in range(n):
#         freq_p[ord(p[c]) - ord('a')] += 1

#     low = 0
#     res = []
#     freq_s = [0]*26 # space: O(1)
    
#     for high in range(len(s)):
#         freq_s[ord(s[high]) - ord('a')] += 1
# # We ensure that size > n only one time in any iteration so we not necessary to use while-loop
#         if (high-low+1) > n:  
#             freq_s[ord(s[low]) - ord('a')] -= 1
#             low += 1
        
#         if (high-low+1) == n and freq_s == freq_p:
#             res.append(low)
    
#     return res

# print(findAnagram('cbabbacb','abc'))


