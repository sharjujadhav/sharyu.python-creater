21.Create a list of numbers and find the sum and average.

l = [4, 5, 1, 2, 9, 7, 10,8]
count = 0
for i in l:
    count +=i
    avg = count/len(l)
    print("sum = " , count)
    print("average = " , avg)
