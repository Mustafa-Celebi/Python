
#! Creating Password between 5-10 digits

username = (input("Enter your username, please: "))

password = (input("Enter your password, please: "))

if not 5 < (len(password)) < 10:
    print("Your passwords lenght have to be 5-10 digits!")
    password = (input("Enter your password, please: "))
    while not 5 < len(password) < 10:
        print("Your passwords lenght have to be 5-10 digits!")
        password = (input("Enter your password, please: "))

if 5 < len(password) < 10:
    print("Your account created succesfully.")