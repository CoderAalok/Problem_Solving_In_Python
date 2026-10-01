from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    
    res = []
    for col in range(len(matrix[0])):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        
        res.append(temp)
    
    return res

matrix = [
    [1,2,3], 
    [3,4,1]
]

print("Original Matrix: ")
for m in matrix:
    print(m)

print("\nTranspose of Matrix: ")
for mt in transpose(matrix):
    print(mt)
