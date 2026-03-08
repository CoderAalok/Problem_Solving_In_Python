# Anagram: Anagram is the same length of a word and its characters called anagram.
# Note: length of a word at least two. 

# Method-I
# # Time Complexity: O(n. klogk) 
# # (n -> Number of word ) 
# # (k -> Average Length of a word)

# def anagram_grouping(words):
#     if not words or len(words) < 2:
#         return []
    
#     anagram = {}
#     for word in words:
#         keyword = "".join(sorted(word)) 

#         if keyword not in anagram:
#             anagram[keyword] = [word]
#         else:
#            anagram[keyword].append(word)

#     return [value for value in anagram.values()]

# words = ['cat', 'ball', 'act', 'tac', 'labl', 'apple','leapp']
# print(anagram_grouping(words))


# Method-II
# Time Complexity: O(n.logk) 
# (n -> Number of word ) 
# (k -> Average Length of a word)

# Frequency based approach (Slighlty more optimal than previous one(Method-I))
def anagram_grouping(words):
    if not words or len(words) < 2:
        return []
    
    anagram = {}
    for word in words:
        keyword = [0]*26 # fixed 26 characters 
        for w in word:
            # characters are holds one by one exact position
            keyword[ord(w) - ord('a')] += 1
        
        key = tuple(keyword) # convert list into tuple due to list is unhashable in dictionary case

        if key not in anagram:
            anagram[key] = [word]
        else:
           anagram[key].append(word)

    return [value for value in anagram.values()]

words = ['cat', 'ball', 'act', 'tac', 'labl', 'apple','leapp']
print(anagram_grouping(words))


