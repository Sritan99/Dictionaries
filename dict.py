d={"apple":"a red friut","banana":"a yellow fruit"}
print(d)

d["strawberry"]= "a red fruit"
print(d)

d["strawberry"]="a fruit with seeds" 
print(d)

# del d["apple"]
# print(d)

if "apple" in d:
    print("Yes")

else:
    print("No")

a=d["apple"]
print(a)