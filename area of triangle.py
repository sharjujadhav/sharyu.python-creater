35.Calculate the area of a triangle using Heron's formula


import math 
a = float(input("enter the length of side a: "))
b = float(input("enter the length of side b: "))
c = float(input("enter the length of side c: "))

s = (a + b + c) / 2
 
area = math.sqrt(s * (S - a) * (S - b) * (s - c))
print("the area of the triangle is :",area)
