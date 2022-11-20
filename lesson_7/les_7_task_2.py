# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random as rnd

my_list = [rnd.randint(0, 49) for _ in range(1, 10)]


def merge_two_list(lst1, lst2):
    """Объединяет два отсортированных списка"""
    c = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            c.append(lst1[i])
            i += 1
        else:
            c.append(lst2[j])
            j += 1
    if i < len(lst1):
        c += lst1[i:]
    if j < len(lst2):
        c += lst2[j:]
    return c


def merge_sort(s):
    """Выполняет сортировку"""
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


print(my_list, merge_sort(my_list))