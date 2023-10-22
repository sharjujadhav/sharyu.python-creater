22.Find the largest and smallest elements in a list.

l = [4, 5, 1, 2, 9, 7, 10,8]
count = 0
for i in l:
    count +=i
    avg = count/len(l)
    print("sum = " , count)
    print("average = " , avg)
