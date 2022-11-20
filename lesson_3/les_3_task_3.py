"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

size = 10
my_list = [random.randint(1, 100) for _ in range(size)]
print(my_list)
max_item = my_list[0]
max_item_idx = 0
min_item = my_list[0]
min_item_idx = 0
for i in range(len(my_list)):
    if max_item <= my_list[i]:
        max_item = my_list[i]
        max_item_idx = i
    if min_item >= my_list[i]:
        min_item = my_list[i]
        min_item_idx = i
my_list[min_item_idx], my_list[max_item_idx] = my_list[max_item_idx], my_list[min_item_idx]
print(my_list)

# задача сформулирована некорректно: непонятен случай, если несколько максимальных или минимальных элементов.
# не всегда будет глобальный минимум или максимум
