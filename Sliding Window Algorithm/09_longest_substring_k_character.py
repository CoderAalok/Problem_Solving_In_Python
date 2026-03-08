def longestSubstringDistinct(strr, k):
    if k <= 0:
        return -1
    
    low, res = 0, -1
    n = len(strr)
    hashmap = {}
    for high in range(n):
        # Expand window size whether adding new character or increment frequency of existing character

        # if strr[high] not in hashmap:
        #     hashmap[strr[high]] = 1 
        # else:
        #     hashmap[strr[high]] += 1 
        
        hashmap[strr[high]] = hashmap.get(strr[high],0) + 1
        
        while len(hashmap) > k:
            # shrink frequency
            hashmap[strr[low]] -= 1
            # remove when frequecy of this character become zero
            if hashmap[strr[low]] == 0:
                del hashmap[strr[low]]
            #shrink window size
            low += 1
        
        if len(hashmap) == k:
            # size of current substring
            size = high - low + 1
            # stored current result
            res = max(res, size)
    
    return res

strr = 'aaaaa'
k = 2
print(longestSubstringDistinct(strr,k))


