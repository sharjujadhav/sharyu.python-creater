59.Count the number of vowels and consonants in a string.

str=input("Please enter a string as you wish: ");
vowels=0
consonants=0
str.lower()
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' ):
           vowels=vowels+1;
    else:
        consonants=consonants+1;
print("The number of vowels:",vowels);
print("\nThe number of consonant:",consonants);
