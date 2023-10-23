79.Find the length of the longest word in a list of words.

from functools import reduce
 
def longestLength(words):
    
    longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
    print("The word with the longest length is:", longest_word, " and length is ", len(longest_word))
  
a = ["one", "two", "third", "four"]
longestLength(a)
