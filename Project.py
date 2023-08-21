#1
def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten_list(input_list)
print(output_list)


#2
def tersine_cevir(liste):
    for i in range(len(liste)):
        liste[i] = liste[i][::-1]
    liste.reverse()
    return liste
input_liste = [[1, 2], [3, 4], [5, 6, 7]]
output_liste = tersine_cevir(input_liste)
print(output_liste)
