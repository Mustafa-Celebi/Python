#At the beginning of the for loop, <variable> takes the value of the first element of <object>. After the code in it runs once, it runs a second time and <variable> takes the value of the second element of <object>. This continues until all elements of <object> are finished.

for x in "hey":
    print(x)



total = 0

for i in range(101):
    total += i

print(total)



total = 1

for a in range(5):
    total *=5

print(total)
#Or you can write like this too:

total = 1

for _ in range(5):
    total *=5

print(total)