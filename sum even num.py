17.Calculate the sum of all even numbers between 1 and N.


num = int(input("enter a number"))
sum = 0
i = 0
while i <= num:
    if i % 2 ==0:
        print (i)
        sum+=i
    i+=1
    print(f"sum of all even numbers is {sum}")
  
