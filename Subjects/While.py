#While uses to create loops. When it is right, it realises the cycle inside it, and this cycle does not stop until we get what we want.

a = 10*2.7
b = 7*9

x = int(input("Write a number please: "))

while x < a:
    print("Try again!")
    x = int(input("Write a number again: "))
if x > a:
    print("Conguratulations you passed first question")
    y = int(input("Write a number for second question: "))
    if "y <= b":
        print("Conguratulations you passed second question too")           
        print("ur very well")
        print(int(input("If you want continue press space write 25 press enter and write 25 at password")))
    t = int(input("Password: "))  
    if t == 25:
        print("Hello. You passed the second level")
elif x == a:
    print("You hit at 12. Lucky!")