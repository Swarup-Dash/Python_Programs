class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            return matrix[i].reverse()
obj=Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Print the original matrix
print("Original matrix:")
for row in matrix:
    print(row)

# Rotate the matrix
obj.rotate(matrix)

# Print the rotated matrix
print("\nRotated matrix:")
for row in matrix:
    print(row)
