print("\n\nTable Generation\n")


initial = int(input("Please enter the initial value:"))
final   = int(input("Please enter the final value  :"))
table = [[0 for col in range(1000)] for row in range(1000)]


for row in range(initial,(final+1)):
    for col in range(initial,(final+1)):
        if row==initial:
            table[row][col] = col
        elif col==initial:
            table[row][col] = row
        else:
            table[row][col] = row*col



for row in range(initial,(final+1)):
    print("\n")
    
    for col in range(initial,(final+1)):
        print(table[row][col]," ",end="")
