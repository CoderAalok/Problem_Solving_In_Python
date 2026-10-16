def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    # edge case
    if not matrix or not matrix[0]:
        return []
    
    left = top = 0
    right = len(matrix[0]) - 1 # length of column (n)
    bottom = len(matrix) - 1 # length of row (m)
    result = []
    
    # Inward Traverse
    while top <= bottom and left <= right:
        # Step 1: left-right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Step 2: top-bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            # Step 3: right-left
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
            
        if left <= right:
            # Step : bottom-top
            for row in range(bottom, top-1 , -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# Test
matrix = [
    [1,2,3,7],
    [4,5,6,1],
    [7,8,9,3],
    [5,1,3,0],
]

# print(spiral_matrix(matrix))
print(len(matrix[0]))

"""
KEY CONCEPT:
1) Left to Right Traverse
2) Top to Bottom Traverse
3) Right to Left Traverse
4) Bottom to Top Traverse
    
    # Until and unless full inward traverse
"""