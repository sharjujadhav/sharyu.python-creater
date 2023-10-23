
60.check if a string is a palindrome. 

def=isPalindrome(s):
    return s == s[::-1]
 
 s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
