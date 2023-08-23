num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))
operator = input("Write what do you want(+,-,x,/): ")
if operator == "+":
    print(num1 + num2)
if operator == "-":
    print(num1-num2)
if operator == "x":
    print(num1*num2)
if operator == "/":
    print(num1/num2)
again = input("Anythink else?(y/n): ")
if again == "y":
    print("Ok! Ask me.")
    num1 = int(input("Write first number: "))
    num2 = int(input("Write second number: "))
    operator = input("Write what do you want(+,-,x,/): ")
    if operator == "+":
        print(num1 + num2)
    if operator == "-":
        print(num1-num2)
    if operator == "x":
        print(num1*num2)
    if operator == "/":
        print(num1/num2)