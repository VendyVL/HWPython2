# Реализуйте алгоритм перемешивания списка.

list = ['green', 'blue', 'red', 'broun', 'orange', 'purple']

list2 = []
a = len(list)
while len(list2) <= a :
    minimal = len(list[0]) # Как 0 может быть out of range?
    imin = 0
    for i in range (0, len(list)):
        if len(list[i]) < minimal: 
            minimal = len(list[i])
            imin = i
        else: i+1 
    list2.append(list[imin])
    list.pop(imin)

print(list)
print(list[imin])
print(list2)
