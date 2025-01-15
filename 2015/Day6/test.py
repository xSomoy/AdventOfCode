import numpy as np
matrix = np.zeros((5, 5))
# print(matrix)
matrix[0][0] = 1
matrix[1][0] = 2
# print(matrix)
sum = 0
for row in matrix:
    for element in row:
        sum += element
print(sum)

if matrix[0][0] == 1:
    print("works")
