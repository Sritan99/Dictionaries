alphabet={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

check=input("Enter a phrase to check if it's a panagram: ").lower()

for i in check:
    if i in alphabet:
        alphabet[i]+=1

print(alphabet)

counter=0
for i in alphabet.values():
    if i >0:
        counter+=1

if counter==26:
    print("Its's a panagram!")

else:
    print("It's not a panagram")