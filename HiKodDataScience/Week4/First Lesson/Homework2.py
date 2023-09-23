
#! How Old Are You? Calculating Age

def info():
    name = input("What's your name?: ")
    def age():
        born = int(input("When did you born?: "))
        age = 2023 - born
        forretire = 65 - age
        if age < 65:
            if forretire == 1:
                print(f"{name}, you have {forretire} year to retire.")
            elif forretire != 1:
                print(f"{name}, you have {forretire} years to retire.")

        elif age >= 65:
            print(f"{name}, you were retired.")
    age()
info()