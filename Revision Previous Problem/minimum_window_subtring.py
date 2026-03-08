def minimum_window(s:str, t:str) -> str:
    # edge case
    if not s or not t:
        return ""
    
    # count each character of frequency containing 't'
    freq_t = {}
    for ch in t:
        freq_t[ch] = freq_t.get(ch, 0) + 1
    
    required = len(freq_t) #requirement characters 
    window = {}
    res = ""
    left = count = 0
    win_size = float('inf')
    
    for right in range(len(s)):
        # count each character of frequency in s
        char = s[right]
        window[char] = window.get(char, 0)+1
        # check window containing char frequency matches to 't' character frequency
        if char in freq_t and window[char] == freq_t[char]:
            count += 1
        
        # check requirement satisfy
        while count == required:
            if (right-left+1) < win_size:
                win_size = right-left+1
                res = s[left : right+1] # 0(k) where k is string
                
            window[s[left]] -= 1
            # shrinked char frequency matches to t-chars frequency
            if s[left] in freq_t and window[s[left]] < freq_t[s[left]]:
                count -= 1
            
            # Is char frequency zero
            if window[s[left]] == 0:
                del window[s[left]]
            
            left += 1
    
    return res

print(minimum_window('cbcabbe','ab'))
