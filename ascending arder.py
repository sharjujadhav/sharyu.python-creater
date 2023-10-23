5.Check if a list is sorted in ascending order.

test_list = [1, 4, 5, 8, 10]
 
print ("Original list : " + str(test_list))
 
flag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        flag = 1
    i += 1
     
if (not flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")
