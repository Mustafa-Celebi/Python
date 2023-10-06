salary = int(input("How much your salary?: "))

if salary <= 10000:
    new_salary = salary - ((salary/100)*5)
    print(new_salary)

elif salary <= 25000:
    new_salary = salary - ((salary/100)*10)
    print(new_salary)

elif salary <= 45000:
    new_salary = salary - ((salary/100)*25)
    print(new_salary)

elif salary > 45000:
    new_salary = salary - ((salary/100)*30)
    print(new_salary)