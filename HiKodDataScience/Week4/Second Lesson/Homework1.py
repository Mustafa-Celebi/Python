
#! Append and Enumerate
list = ["1",3,"2",10,"3",9,"4","5","6","7"]
new_list = []

for i, element in enumerate(list):
    if type(element) == str:
        new_list.append(element)
print(new_list)


#! Printing Students Notes
students = {

    "John":{"Maths": 80,"Chemistry": 85,"PE": 100},
    "Rebecca":{"Maths": 100,"Chemistry": 70,"PE": 100},
    "Adrien":{"Maths": 90,"Chemistry": 83,"PE": 100},
}

name = input("Write student name: ")
lesson = input("Write lesson name: ")

if name in students:
    try:
        note = students[name][lesson]
        print(f"{name}'s note for {lesson} is {note}.")
    except KeyError:
        print(f"{name}'s note not found in {lesson} lesson.")
else:
    print(f"{name} isn't found")