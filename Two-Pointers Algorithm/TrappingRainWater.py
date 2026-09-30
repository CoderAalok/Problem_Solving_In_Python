def trapArea(height: List[int]) -> int:
    """Non empty, non-negative integer height"""
    left, right =  0, len(height) - 1
    left_max = right_max = res = 0
    
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            res += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            res += right_max - height[right]
            right -= 1
    
    return res


# Test Cases
# height = [2,0,4,6]
# height = [9,7,0,2,8,4,0,6]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapArea(height))


"""
Time Complexity: O(n)
Space Complexity: O(1) # Constant space(No space) used
"""

# Thought process: 
"""How much water it can trap after raining?  -> Meaning water trap only those area where there is gaps.  
"""
"TARGET: How can we calculate those gaps?" "-> Result"
"Can we use pointers?" "-> Obviously, yes because water setting on top of bars aas well as button held by both sides."

"""Set fix the pointers at start and end index, 
                |
Now which pointer move and how to move? 
                |
Comparision both height and move though shortest height of bar(because of limiting factor)
Keep hold tallest/maximum height either on left or right side (meaning if get shortest height (i.e left), 
so the tallest height on left side height[left] otherwise, height[right] ).
                |
After this move inward left or right(depending upon current shortest  height either on (left or right))
"""

"""DRY RUN

height = [2,0,4,6]
          0,1,2,3
          
left, right = 0, 3
left_max = 2, right_max = 6
res += left_max  - hight[left] = 2 - 2 = 0 (no water trap here)
left += 1

res += left_max  - hight[left] = 2 - 0 = 2
left += 1

res += left_max  - hight[left] = 2 - 4 = -2 (no water trap here)
left += 1

left = 3, right = 3 [condition FALSE]

res = 2
"""