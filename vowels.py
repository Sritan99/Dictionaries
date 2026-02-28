vowel={"a":0,"e":0,"i":0,"o":0,"u":0}
word=input("What word would you like to count the vowels of? ")

for i in word:
    print(i)
    if i in vowel:
       vowel[i]=vowel[i]+1
       
print(vowel)

