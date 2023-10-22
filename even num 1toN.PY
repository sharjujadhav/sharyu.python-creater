15.Print even numbers from 1 to N using a for loop.

maximum = int(input("enter a maximum value:"))
for num in range(1, maximum+1):
    if(num%2==0):
        print("{0}".format(num))
