def rotate_compare(s1: str, s2: str) -> int:
    """Obtained s2 by left rotation of s1"""
    # edge case
    if (not s1) or (not s2) or (len(s1) != len(s2)):
        return -1
    
    if s1 == s2:
        return 0
    
    for i in range(len(s1)):
        rotate = s1[i+1: ] + s1[:i+1]
        if rotate == s2:
            return i + 1
        
    return -1

s1 = "coding"
s2 = "dingco"
print(rotate_compare(s1, s2))