# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
with open('file.txt', 'w') as data:
 data.write('2\n')
 data.write('-3\n')

# Файл создаётся за пределами папки где у меня git

n = int(input('Введите число N = '))

if n<0: n=-n

def numList(n):
    num_list = []
    i = 0
    for a in range(-n,n+1):
       num_list.append(a)
       i +=1
    return num_list

list = numList(n)
print(list)
    
file = 'file.txt'
d = open (file, 'r')
l2 = []
i=0
for line in d:
    l2.append(line)

a = int(l2[0])
b = int(l2[1])

res = list[a]*list[b]

print (res)