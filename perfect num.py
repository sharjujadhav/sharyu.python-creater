40.Check if a number is a perfect number

n = 28
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum +1
if sum == n:
    print("the number is a perfect number")
else:
    print("the number is not a perfect number")
