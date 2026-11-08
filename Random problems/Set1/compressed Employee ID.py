def compressed_id(s: str) -> str:
    result, count = s[0], 1  # s -> Non-empty 
    for i in range(1, len(s)):
        # count frequency of character
        if s[i] == result[-1]:
            count += 1
        
        # update result and count
        else:
            if count > 1:
                result += str(count)  # compresse character
            
            result += s[i]  # add new character
            count = 1 # reset count
    
    result += str(count)
    return result 


print(compressed_id('aaabbc1111xiiaaggao111a'))