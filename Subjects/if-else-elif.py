a = 10*2.7
b = 7*9

x = int(input("Write a number please: "))

if x > a:
    print("Conguratulations you passed first question")
    y = int(input("Write a number again: "))
    if "y <= b":
        print("Conguratulations you passed second question too")
        print("ur very well")
        print(int(input("If you want continue press space write 25 press enter and write 25 at password")))
        t = int(input("Password: "))  
        if t == 25:
            print("Hello. You passed the second level")
elif x == a:
    print("You hit at 12. Lucky!")
else:
        print("Try again.")