from typing import List
def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # A = l * h -> distance between two lines * minimum(height)
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

height = [2,7,4,8,10]
print(maxArea(height))

" DRY RUN: "
"""
left = 0, right = 4
max_area = 0
area = (4-0) * min(height[0], height[4]) = 4 * 2 = 8
max_area = 8
# condition : 2 < 10 (True)
left += 1


left = 1, right = 4
max_area = 8
area = (4-1) * min(height[1], height[4]) = 3 * 7 = 21
max_area = 21
# condition : 7 < 10 (True)
left += 1


left = 2, right = 4
max_area = 21
area = (4-2) * min(height[2], height[4]) = 2 * 4 = 8
max_area = 21
# condition : 4 < 10 (True)
left += 1


left = 3, right = 4
max_area = 21
area = (4-3) * min(height[3], height[4]) = 1 * 8 = 8
max_area = 21
# condition : 8 < 10 (True)
left += 1


left = 4, right = 4
# condition: left < right (False)

# Final answer:
return max_area -> 21

"""