def longestPalindrome(s: str) -> str:
    max_size, palindrome = 0, ""
    for i in range(len(s)): # O(n)
        for j in range(len(s) - 1, i-1, -1): # O(n)
            if s[i : j + 1][ :: -1] == s[i : j + 1]: # O(n)
                if (j - i + 1) > max_size:
                    palindrome = s[i : j + 1]
                    max_size = j - i + 1
                
    return palindrome
    
s = "abbaca"
print(longestPalindrome(s))


"""
Time Complexity: O(n^3)  -> wrost
Space Complexity : O(1)
"""
