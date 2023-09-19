
#! Creating Password and Username to Log In

username = input("Create an username: ")

password = input("Create a password: ")

password_login = input("What is your password?: ")

if password == password_login:
    print("Logged in succesfully!")

else:
    remaining_entry_right = 3
    while password != password_login:
        print("You write false password!!")
        remaining_entry_right -= 1
        print(f"You have {remaining_entry_right} entries left")
        if remaining_entry_right == 0:
            print("Log in failed...")
            break
        password_login = input("What is your password?: ")
        if password == password_login:
            print("Logged in succesfully!")