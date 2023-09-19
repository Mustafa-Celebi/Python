
#! Creating Password
username = (input("Enter your username, please: "))

password = (input("Enter your password, please: "))

if (len(password)) < 6:
    print("Your passwords lenght have to 6 digits at least!")
    password = (input("Enter your password, please: "))
    if (len(password)) >= 6:
        print("Your account created succesfully.")

elif len(password) >= 6:
    print("Your account created succesfully.")