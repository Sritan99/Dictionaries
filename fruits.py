fruits={}
friend=[]
for i in range (5):
 f=input("What is your favrioute fruit? ")
 friend.append(f)

print(friend)

for i in friend:
    if i in fruits:
       fruits[i]=fruits[i]+1
    
    else:
       fruits[i]=1

print(fruits)
 
 
