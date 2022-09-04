# Реализуйте алгоритм перемешивания списка.

list = ['green', 'blue', 'red', 'broun', 'orange', 'purple']

list2 = []
minimal = len(list[0])
imin = 0
while len(list2) <= len(list):
    for i in range (0, len(list)):
        if len(list[i]) < minimal and list[i]!="0": # Я не понимаю почему оно не выполняет условие неравенства
            minimal = len(list[i])
            imin = i
        else: i+1 
    list2.append(list[imin])
    list[imin] = "0"

print(list)
print(list[imin])
print(list2)
