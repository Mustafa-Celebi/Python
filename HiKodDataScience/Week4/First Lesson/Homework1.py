
#! Calculating Area Of The Circle
pi_number = float(input("How much is the π value?: "))

radius = float(input("How much is the radius?: "))

def areaofthecircle():
    return pi_number * (radius ** 2)

print(areaofthecircle())

#! Calculating Factorial
def factorial(x):
    factorial = 1
    for _ in range(1, x + 1):
        factorial *= _
    return factorial

number = int(input("Write the number whose factorial you want to calculate: "))
factorial = factorial(number)

print("{}! = {}".format(number, factorial))