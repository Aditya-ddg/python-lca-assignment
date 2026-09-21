# Program to add two matrices

# Create two matrices
matrix1 = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9] 
] 
matrix2 = [ 
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# Create an empty matrix for the result
result = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0] 
]
# Add the two matrices
for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j] 
# Display the matrices 
print("First Matrix:")
for row in matrix1:
    print(row) 
print("\nSecond Matrix:") 
for row in matrix2: 
print(row)
print("\nSum of Two Matrices:")
for row in result:
print(row)
