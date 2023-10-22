11.Write a program to check if a number is prime

num1 = int(input("enter a first number"))

if num1>1:
    for i in range (2, int (num1/2)):
        if (num1%i ==0):
            print(f"{num1} is not a prime number")
            break
else:
    print(f"{num1} is a prime number")
