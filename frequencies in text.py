67.Create a dictionary of words and their frequencies in a text.

test_string=raw_input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))
