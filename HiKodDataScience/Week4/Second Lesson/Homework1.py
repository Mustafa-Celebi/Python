
#! Append and Enumerate
list = ["1",3,"2",10,"3",9,"4","5","6","7"]
new_list = []

for i, element in enumerate(list):
    if type(element) == str:
        new_list.append(element)
print(new_list)