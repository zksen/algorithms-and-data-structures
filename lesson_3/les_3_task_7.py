"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться."""
import random

size = 10
my_list = [random.randint(1, 10) for _ in range(size)]

min1 = my_list[0]
pos = 0

for i in range(len(my_list)):
    if my_list[i] < min1:
        pos = i
        min1 = my_list[i]

if pos != 0:
    min2 = my_list[0]
else:
    min2 = my_list[1]

for i in range(len(my_list)):
    if my_list[i] < min2 and i != pos:
        min2 = my_list[i]

print(f'Список: {my_list}, первый минимальный: {min1}, второй минимальный: {min2}')