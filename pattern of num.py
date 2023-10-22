31.Print a pattern of numbers in an equilateral triangle.


n=20
for i in range(1, 11):
        print(' '*n,end='')
        
        print('* '*(i))
        n-=1
