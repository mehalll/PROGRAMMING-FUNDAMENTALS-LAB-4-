print("\n\nMatrix Addition\n")

matrix1 = [[row*col for col in range(1,4)] for row in range(1,4)]
matrix2 = [[row+col for col in range(1,4)] for row in range(1,4)]
add     = [[0 for col in range(1,4)] for row in range(1,4)]
print("\n\nMatrix1",end=":")    
for row in range(3):
    print("\n",end="")
    for col in range(3):
        print(matrix1[row][col],end=" ")   
        
print("\n\nMatrix2",end=":")        
for row in range(3):
    print("\n",end="")
    for col in range(3):
        print(matrix2[row][col],end=" ")         
        
        
for row in range(3):
    for col in range(3):
        add[row][col] = int(matrix1[row][col]) + int(matrix2[row][col])
        
print("\n\nAddition of Matrix1 and Matrix2",end=":")        
for row in range(3):
    print("\n",end="")
    for col in range(3):
        print(add[row][col],end=" ")
