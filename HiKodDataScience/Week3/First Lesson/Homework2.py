
#! Giving Variable

name1 = "Ahmet"
age1 = 36

name2 = "Zehra"
age2 = 23

name3 = "Süleyman"
age3 = 16

#! Logical Comparisons
print(age1 == age2 or age1 == age3)
#? False

print(age2 != age3 and len(name2) == len(name3))
#? False

print(len(name1) == len(name2) or age3 < age1)
#? True

print(age2>age3 and len(name1) < len(name3))
#? True

print(age2 < age3 or age3 > len(name3) or name1 == name2)
#? True