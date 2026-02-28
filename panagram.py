alphabet={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}

check=(input("Enter a number to check if it's a number panagram "))

for i in check:
    if i in alphabet:
        alphabet[i]+=1

print(alphabet)

counter=0
for i in alphabet.values():
    if i >0:
        counter+=1

if counter==10:
    print("Its's a number panagram!")

else:
    print("It's not a number panagram")



          