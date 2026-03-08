# Problem-III

# The main approach to learn or remember of this problem ->
# Assume too larger number because which helps to find easily,
# whenever given element non-negative or negative.

# Method-I
# def second_largest_element(arr):
#     if not arr or len(arr) < 2:
#         return None
    
#     large_element = second_element = -1  # Assume
#     # first we find largest element, after found,
#     # befor the previous large_element stored into second_element(becaue may it have second largest element)
#     for x in arr:
#         if x > large_element:
#             second_element = large_element
#             large_element = x
            
#         elif second_element < x < large_element:
#             second_element = x
            
#     return second_element

# arr = [1,5,0,9,8]
# print(second_largest_element(arr))

# Method-II  (Optimal solution)
def second_largest_element(arr):
    if not arr or len(arr) < 2:
        return None
    
    # Assume too large negative because our main target to
    # find second largest element either that element negative or non-negative.
    large_element = second_element = float('-inf') 
    
    for x in arr:
        # First condition: Assume x -> largest element
        if x > large_element:
            second_element = large_element  #large_element -> may it second largest element
            large_element = x # May it largest element
        
        # Second condition: Assume x -> non-largest element that is it may second largest element
        elif second_element < x < large_element:
            second_element = x

    return second_element

arr = [-1,-5,-3,5]
print(second_largest_element(arr))


# # Method-III
# def second_largest_element(arr):
#     if not arr or len(arr) < 2:
#         return None
    
#     largest_element = max(arr)
#     second_element = float('-inf')
#     for x in arr:
#         if second_element < x < largest_element:
#             second_element = x

#     return second_element

# arr = [-1,-5,-3,5,8]
# print(second_largest_element(arr))
