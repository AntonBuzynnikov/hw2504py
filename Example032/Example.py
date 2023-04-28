# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
_min = int(input("Введите минимум: "))
_max = int(input("Введите максимум: "))
n = 10
list_1 = [randint(1,100) for i in range(n)]
list_2 = list()
for i in range(len(list_1)):
    if list_1[i]>=_min and list_1[i]<=_max:
        list_2.append(i)
print(list_2)