9. Write a program to find a maximum of three numbers.

num1 = int(input("enter a first number"))
num2 = int(input("enter a second number"))
num3 = int(input("enter a third number"))
if num1>=num2 and num1>=num3:
    print(f"{num1} is greater")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

