62.Reverse the order of words in a sentence

string = "geeks quiz practice code"

s = string.split()[::-1]
l = []
for i in s:
   
    l.append(i)
print(" ".join(l))
