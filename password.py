user_pass={"user_1":"123456","bob":"ABC123","Adam":"09876"}

user=input("What is your username? ")

if user in user_pass:
    password=input("What is your password? ")
    if password==user_pass[user]:
        print("You have logged in.")

    else:
        print("That is the wrong password.")
        
else:
    print("That is not available")





