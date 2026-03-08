# # Problem-IV
# # Palindrome: The reversed of element same as original state.

# # For string:
# # Method-I
# def Is_Palindrome(strr):
#     strr = strr.replace(" ","").lower() #Ignore empty and white spaces
#     if strr == "" or len(strr) < 2:
#         return None
    
#     rev = ""
#     size = len(strr)
#     for p in range(1, size+1):
#         rev += strr[size-p] #with preserved order to reversed
        
#     return rev == strr

# strr = 'aabaa'
# print(Is_Palindrome(strr))

# # Method-II (Optimal)
# def Is_Palindrome(strr):
#     strr = strr.replace(" ","").lower()
#     if strr == "" or len(strr) < 2: #Ignore spaces and empty
#         return None
    
#     is_palindrome = strr[::-1] == strr

#     return is_palindrome

# strr = 'asdfnfdsa'
# print(Is_Palindrome(strr))


# For number:
def Is_palindrome(num):
    if num <= 1:
        return False
    
    rev = 0
    new_num = num
    while num != 0:
        rev = rev*10 + (num % 10)
        num = num//10

    if new_num == rev:
        return True
    else:
        return False
    
num = 2120
print(Is_palindrome(num))
        