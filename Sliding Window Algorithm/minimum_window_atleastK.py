def minimum_window(s:str, k:int) -> int:
    # edge case 
    if not s or k <= 0:
        return 0
    
    
    left = 0
    min_window = float('inf')
    window = {}
    # res = ""
    
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        while len(window) >= k:
            min_window = min(min_window, right-left+1)
            # if (right-left+1) < win_size:
                # res = s[left:right+1]
            
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            
            left += 1
    
    return 0 if min_window == float('inf') else min_window

print(minimum_window('aaaaa',2))