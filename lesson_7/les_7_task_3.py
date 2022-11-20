# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой — не больше медианы.

import random as rnd

size = 2 * rnd.randint(1, 100) + 1
l = [rnd.randint(0, 1000) for _ in range(1, size + 1)]
print(l)


# def nlogn_median(l):
#     l = sorted(l)
#     if len(l) % 2 == 1:
#         return l[int(len(l) / 2)]
#     else:
#         return 0.5 * (l[int(len(l) / 2 - 1)] + l[int(len(l) / 2)])


def quickselect_median(l, pivot_fn=rnd.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


print(sorted(l))
print(f'Медиана {quickselect_median(l)}')