student_1 = 78
student_2 = 80
student_3 = 43
student_4 = 65
student_5 = 90

#I can descript it also like this:

notes = [78, 80, 43, 65, 90]

#If I want student 1's note i should write:

print(notes[0])

#If i wanna change 2. student's note i should write:

notes[1] = 85
print(notes)

#Indexing and Slicing

print(notes[-1])
#-90


#If we give 10 to range we give index out of yhe range error.


print(notes[0])


print(notes[0:3])
#[78 85 43]


print(notes[:3])
#[78 85 43]


print(notes[:2000])
#[78, 85, 43, 65, 90]