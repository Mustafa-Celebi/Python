
#! Using Split
name = "Hi-Kod Veri Bilimi Atölyesi"
print(name)

name_split = name.split()
print(name_split)

#! Making all letters big
name_upper = name.upper()
print(name_upper)
#? Output = HI-KOD VERI BILIMI ATÖLYESI

#! Making all letters small
name_lower = name.lower()
print(name_lower)
#? Output = hi-kod veri bilimi atölyesi

#! Choosing even numbers
list = "0123456789"
list2 = [i for i in list if int(i) % 2 == 0]
print(list2)
#? Output = ['0', '2', '4', '6', '8']

#! Choosing odd numbers
list = "0123456789"
list2 = [i for i in list if int(i) % 2 != 0]
print(list2)
#? Output = ['1', '3', '5', '7', '9']
