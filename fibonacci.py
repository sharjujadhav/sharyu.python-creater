18.Generate a Fibonacci sequence up to N terms.


num = int(input("enter a number"))
n1 = 0
n2 = 1
for i in range (1 , num):
    num3 = n1 + n2
    print(num3)
    n1,n2 = n2 , num3
