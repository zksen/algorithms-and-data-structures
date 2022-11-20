"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать."""
import random

size = 10
my_list = [random.randint(1, 10) for _ in range(size)]
max_el = my_list[0]
pos1 = 0
min_el = my_list[0]
pos2 = 0
my_sum = 0
for i in range(len(my_list)):
    if my_list[i] < min_el:
        min_el = my_list[i]
        pos2 = i
    if my_list[i] > max_el:
        max_el = my_list[i]
        pos1 = i

if pos1 > pos2:
    for i in range(pos2 + 1, pos1):
        my_sum += my_list[i]
else:
    for i in range(pos1 + 1, pos2):
        my_sum += my_list[i]

print(
    f'Массив: {my_list}, минимальный и его позиция: {(min_el, pos2)}, максимальный и его позиция: {(max_el, pos1)}, сумма элементов между: {my_sum}')
