## Matrix using Nested Lists 

A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("2nd row",A[1])
print("3rd row 2nd element",A[2][1])
print("1st row last element",A[0][-1])

print("2nd column")
column = []
for row in A:
    column.append(row[1])
print(column)

################################  Adding  2 matrices  ###################################
B = [[3,4,5,6],
     [7,8,9,10],
     [11,12,13,14]]

AandB = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(A)):
    for j in range(len(A[0])):
            AandB[i][j] = A[i][j] + B[i][j] 

# List comprehension 
AandBLC = [[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]


print(AandB)
print(AandBLC)

################################  Matrix Multiply ###################################
