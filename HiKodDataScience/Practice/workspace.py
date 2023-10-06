meyveler = ("armut","muz","ayva","portakal","armut","mandalina")
index = 0
while index < len(meyveler):
    print(f"{meyveler[index]}")
    index += 1

    musteri_bilgileri = {"ayşe yılmaz":"456321",
                    "mine sönmez":"741258",
                    "emir alpay" : "456987",
                    "sevim kara" : "369852"}
a = input("Ad giriniz: ")
print(musteri_bilgileri[a])


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
    print(f"{name} isn't found")