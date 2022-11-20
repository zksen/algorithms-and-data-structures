# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в
# файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# print(sys.version, sys.platform)
# 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] win32

import sys
import random as rnd


def show_size(x, level=0):
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')

    if hasattr(x, '__iter__'):

        if hasattr(x, 'items'):

            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)

        elif not isinstance(x, str):

            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)

    return size_par


# Первый алгоритм
l1 = [rnd.randint(1, 10000) for _ in range(1, 20)]
max_item = l1[0]
max_item_idx = 0
min_item = l1[0]
min_item_idx = 0

for i in range(len(l1)):

    if max_item <= l1[i]:
        max_item = l1[i]
        max_item_idx = i

    if min_item >= l1[i]:
        min_item = l1[i]
        min_item_idx = i

l1[min_item_idx], l1[max_item_idx] = l1[max_item_idx], l1[min_item_idx]

sum_member1 = show_size(max_item) + show_size(min_item) + show_size(max_item_idx) + show_size(min_item_idx) + show_size(
    l1)
print('В 1 программе задействовано байт памяти: {}'.format(sum_member1))
# В 1 программе задействовано байт памяти: 892
# Данный алгоритм записывает в память список и 4 объекта типа целое число. Он оптимальнее 2-го и не намного больше
# памяти занимает по сравнению с третьим

# Второй алгоритм
l2 = [rnd.randint(1, 10000) for _ in range(1, 20)]
l22 = l2[:]
l2.sort()
l22[l22.index(l2[0])], l22[l22.index(l2[-1])] = l22[l22.index(l2[-1])], l22[l22.index(l2[0])]
sum_member2 = show_size(l2) + show_size(l22)
print('Во 2 программе задействовано байт памяти: {}'.format(sum_member2))
# Во 2 программе задействовано байт памяти: 1520
# Данный алгоритм не оптимален по памяти, потому что сохраняет один и тот же список дважды

# Третий алгоритм
l3 = [rnd.randint(1, 10000) for _ in range(1, 20)]
l3[l3.index(min(l3))], l3[l3.index(max(l3))] = l3[l3.index(max(l3))], l3[l3.index(min(l3))]
sum_member3 = show_size(l3)
print('В 3 программе задействовано байт памяти: {}'.format(sum_member3))
# В 3 программе задействовано байт памяти: 780
# Данный алгоритм самый оптимальный, потому что задействует память под один список


# Вывод: оптимальнее по памяти среди трех алгоритмов будут алгоритмы под 1 и 3 номером.
# 2 алгоритм будет использовать память вдвое больше, чем 1 и 3, так как работает засчет отдельно
# записанного списка в память