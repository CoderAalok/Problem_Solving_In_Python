# def minimumWindowSubstring(s:str, t:str)-> str:
#     # edge case
#     if not t or not s:
#         return ""
    
#     freq_t = {} # count all possible frequency
#     for ch in t:
#         freq_t[ch] = freq_t.get(ch, 0) + 1
    
#     low = count = 0
#     res = ""
#     window = {}
#     required = len(freq_t)
#     old_size = float('inf') # window size
    
#     for high in range(len(s)):
#         # creates a window
#         char = s[high]
#         window[char] = window.get(char, 0) + 1
#         # check window covers all characters 
#         if char in freq_t and window[char] == freq_t[char]:
#             count += 1 #count -> including frequency of character t
        
#         # after all characters covers window
#         while count == required:
#             # stored current result
#             new_size = high-low+1
#             if new_size < old_size:
#                 old_size = min(old_size, new_size)
#                 res = s[low : high+1]
            
#             # shrink
#             window[s[low]] -= 1
#             # check low character frequency less than t-character frequency
#             if s[low] in freq_t and window[s[low]] < freq_t[s[low]]:
#                 count -= 1
            
#             # check window containing character freq becomes zero
#             if window[s[low]] == 0:
#                 del window[s[low]]
            
#             low += 1
        
#     return res

# print(minimumWindowSubstring('cbacbbe', 'abc'))


def minimum_window(s:str, t:str)-> str:
    if not s or not t:
        return ""
    
    freq_t = [0]*256
    for ch in t:
        freq_t[ord(ch)] += 1  #counting frequency of t-characters
    
    required = 0
    for f in freq_t:
        if f > 0:
            required += 1
    # required = len(set(t))
    
    window = [0]*256
    low = count = 0
    res = ""
    win_size = float('inf')
    
    for high in range(len(s)):
        char = s[high]
        window[ord(char)] += 1
        
        if freq_t[ord(char)] and window[ord(char)] == freq_t[ord(char)]:
            count += 1
        
        while count == required:
            if (high-low+1) < win_size:
                win_size = high-low+1
                res = s[low:high+1]
            
            window[ord(s[low])] -= 1
            if freq_t[ord(s[low])] and window[ord(s[low])] < freq_t[ord(s[low])]:
                count -= 1
            
            low += 1
        
    return res

print(minimum_window('caabacbbe', 'abc'))
