from typing import List
class Solution:
    def rotateImage(self, matrix:List[List[int]]) -> List[List[int]]:
        # Only modify original matrix
        
        # Approach-I: column-wise rotate (using extra space)
        # rotated = []
        # for j in range(len(matrix)):
        #     temp = []
        #     for i in range(len(matrix)-1, -1 , -1):
        #         temp.append(matrix[i][j])
            
        #     rotated.append(temp)
        
        # for i in range(len(matrix)):
        #     matrix[i] = rotated[i]

        # # Approach-II: Transpose and reverse  (constant space)
        # Step 1: Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse the matrix (row-wise)
        for row in matrix:
            row.reverse()
        
        return matrix
        

s = Solution()
matrix = [
    [2,1,5,6],
    [5,3,6,1],
    [6,2,7,8],
    [8,4,2,9]]

res = (s.rotateImage(matrix))
for r in res:
    print(r, end="\n")
