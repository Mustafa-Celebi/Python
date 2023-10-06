
#! Printing Students Notes
students = {

    "John":{"Maths": 80,"Chemistry": 85,"PE": 100},
    "Rebecca":{"Maths": 100,"Chemistry": 70,"PE": 100},
    "Adrien":{"Maths": 90,"Chemistry": 83,"PE": 100},
}

name = input("Write student name: ")
lesson = input("Write lesson name: ")

if name in students:
    note = students[name][lesson]
    print(f"{name}'s note for {lesson} is {note}.")
else:
    print(f"{name} note isn't found")