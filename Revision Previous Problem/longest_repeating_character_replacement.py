def character_replacement(s, k):
    low = max_freq = 0   # preserved the maximum frequency
    res = float('-inf')
    freq = [0]*26
    
    for high in range(len(s)):
        inx = ord(s[high])-ord('A')
        freq[inx] += 1
        max_freq = max(max_freq, freq[inx])
        
        while (high-low+1) - max_freq > k:
            freq[ord(s[low])-ord('A')] -= 1
            low += 1
        
        res = max(res,high-low+1)
    
    return res

s = 'AABBABBA'
k = 2
print(character_replacement(s,k))