"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
import random
size = 15
my_list = [random.randint(-10,10) for _ in range(size)]
my_list2 = [[my_list[idx], idx] for idx in range(len(my_list)) if my_list[idx] < 0]
max_lower = my_list2[0][0]
pos = 0
for eq in range(len(my_list2)):
    if max_lower <= my_list2[eq][0]:
        max_lower = my_list2[eq][0]
        pos = my_list2[eq][1]
print(my_list)
print(f'Максимальный отрицательный элемент: {max_lower} стоит на позиции: {pos}')