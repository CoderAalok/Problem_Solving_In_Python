def longest_substring(s):
    low = res = 0
    hashset = set()
    for high,char in enumerate(s):
        while char in hashset:
            hashset.remove(s[low])
            low += 1
        hashset.add(char)
        res = max(res, high-low+1)
    
    return res
s = 'abacdb'
print(longest_substring(s))