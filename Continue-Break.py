#It provides we can pause the loop (Break)

for i in range(10):
    if i == 3:
        break
    print(i)


x = 0

while x < 10:
    x += 1
    if x == 3:
        break
    print(x)


#It provides to skip a thing like this:

for i in range(10):

    if i == 3:
        continue
    print(i)
