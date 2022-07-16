# Реализуйте алгоритм перемешивания списка.

# А это вообще у нас было? На лекции? Точно не на первой. Там и предыдущей задачи не было.


list = ['red', 'green', 'blue', 'broun']


list2 = []
while len(list)!=0:
    min = len(list[0])
    imin = 0
    for i in range (0, len(list)+1):
        if len(list[i])<min:                 #list index out of range
            min = len(list[i]) 
            imin = i
        list2.append(list[imin])
        list.pop(imin)

print(list)
print(list2)