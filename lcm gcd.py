19.Calculate the LCM and GCD of two numbers.

print("enter two numbers:", end="")
no = int(input())
nt = int(input())

a = no
b = nt
while b!=0:
    temp = b
    b = a%b
    a = temp
gcd = a 
lcm = int((no*nt)/gcd)

print("\nlcm (" +str(no) +"," + str(nt) +") = ",lcm)
print("gcd(" + str(no) + "," + str(nt) +") =" , gcd)
