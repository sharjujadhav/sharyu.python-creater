12.Calculate the factorial of a number.

m1 = int(input("enter a first number"))
fact = 1
if num1 <0:
    print("does not find factorial of negative number")
elif num1 ==0:
    print("factorial of 0 is 1")
    for i in range (1 , num1+1):
        fact = fact*i
        print(f"factorial of {num1} is {fact}")
