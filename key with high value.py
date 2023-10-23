69.Find the keys with the highest values in a dictionary.

dictt = {'1': 100, '2': 1292, '3': 88}  
  
Key_max = max(zip(dictt.values(), dictt.keys()))[1]  
print("The key with the maximum value is: ", Key_max) 
