32. Print a pattern of stars in a diamond shape.

row = int(input('enter number of rows: '))

for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()
for i in range(row-1,0, -1):
    for j in range(1, row-i+1):
        print(" ", end="")
    for i in range(1, 2*i):
        print("*", end="")
    print()
