"""1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков."""


# Отдельно записал списки, чтобы не испортить чистоту эксперимента рандомным созданием списка
# В данной выборке списки длинной: 10, 20, 100, 500, 1000 соответственно
import cProfile
import lists
import lists2


def rev1(l):
    """Первый алгоритм. O(n)"""

    max_item = l[0]
    max_item_idx = 0
    min_item = l[0]
    min_item_idx = 0

    for i in range(len(l)):

        if max_item <= l[i]:
            max_item = l[i]
            max_item_idx = i

        if min_item >= l[i]:
            min_item = l[i]
            min_item_idx = i

    l[min_item_idx], l[max_item_idx] = l[max_item_idx], l[min_item_idx]


# def main_rev1():
#    for item in lists2.my_list:
#        rev1(item)


# Тест на массивах с максимально разными элементами (массивы сгенерированы изначально)
# 1000 разных массивов длиной 1000
# *****************************************
# "les_4_task_1.main_rev1()"
# 1 loop, best of 5: 296 msec per loop
# *****************************************


# Тест на массивах с максимально разными элементами (массивы сгенерированы изначально)
# 1000 разных массивов длиной 10000
# *****************************************
# "les_4_task_1.main_rev1()"
# 1 loop, best of 5: 3.33 sec per loop
# *****************************************


# Тест на плохой выборке (массивы почти из одинаковых элементов)
# длины массивов 10, 20, 100, 500, 1000 соответственно
# *****************************************
# "les_4_task_1.rev1(lists.my_list10)"
# 1000 loops, best of 5: 2.21 usec per loop
# "les_4_task_1.rev1(lists.my_list20)"
# 1000 loops, best of 5: 3.34 usec per loop
# "les_4_task_1.rev1(lists.my_list100)"
# 1000 loops, best of 5: 13.4 usec per loop
# "les_4_task_1.rev1(lists.my_list500)"
# 1000 loops, best of 5: 67.5 usec per loop
# "les_4_task_1.rev1(lists.my_list1000)"
# 1000 loops, best of 5: 133 usec per loop
# *********************************************


def rev2(l):
    """Второй алгоритм O(nlog(n))"""

    l1 = l[:]
    l.sort()
    l1[l1.index(l[0])], l1[l1.index(l[len(l) - 1])] = l1[l1.index(l[len(l) - 1])], l1[l1.index(l[0])]


# def main_rev2():
#     for item in lists2.my_list:
#        rev2(item)


# Тест на массивах с максимально разными элементами (массивы сгенерированы изначально)
# 1000 разных массивов длиной 1000
# *****************************************
# "les_4_task_1.main_rev2()"
# 1 loop, best of 5: 93.6 msec per loop
# *****************************************


# Тест на массивах с максимально разными элементами (массивы сгенерированы изначально)
# 1000 разных массивов длиной 10000
# *****************************************
# "les_4_task_1.main_rev2()"
# 1 loop, best of 5: 1.07 sec per loop
# :0: UserWarning: The test results are likely unreliable. The worst time (4.59 sec) was more than four times slower than the best time (1.07 sec).
# *****************************************


# Тест на плохой выборке (массивы почти из одинаковых элементов)
# длины массивов 10, 20, 100, 500, 1000 соответственно
# *****************************************
# "les_4_task_1.rev2(lists.my_list10)"
# 1000 loops, best of 5: 1.12 usec per loop
# "les_4_task_1.rev2(lists.my_list20)"
# 1000 loops, best of 5: 1.29 usec per loop
# "les_4_task_1.rev2(lists.my_list100)"
# 1000 loops, best of 5: 3.26 usec per loop
# "les_4_task_1.rev2(lists.my_list500)"
# 1000 loops, best of 5: 12.6 usec per loop
# "les_4_task_1.rev2(lists.my_list1000)"
# 1000 loops, best of 5: 24.9 usec per loop
# *********************************************

def rev3(l):
    """Третий алгоритм O(n)"""

    l[l.index(min(l))], l[l.index(max(l))] = l[l.index(max(l))], l[l.index(min(l))]


# def main_rev3():
#   for item in lists2.my_list:
#       rev3(item)



# Тест на массивах с максимально разными элементами (массивы сгенерированы изначально)
# 1000 разных массивов длиной 1000
# *****************************************
# "les_4_task_1.main_rev3()"
# 1 loop, best of 5: 281 msec per loop
# *****************************************



# Тест на массивах с максимально разными элементами (массивы сгенерированы изначально)
# 1000 разных массивов длиной 10000
# *****************************************
# "les_4_task_1.main_rev3()"
# 1 loop, best of 5: 3.48 sec per loop
# *****************************************



# Тест на плохой выборке (массивы почти из одинаковых элементов)
# длины массивов 10, 20, 100, 500, 1000 соответственно
# *****************************************
# "les_4_task_1.rev3(lists.my_list10)"
# 1000 loops, best of 5: 1.71 usec per loop
# "les_4_task_1.rev3(lists.my_list20)"
# 1000 loops, best of 5: 2.37 usec per loop
# "les_4_task_1.rev3(lists.my_list100)"
# 1000 loops, best of 5: 8.31 usec per loop
# "les_4_task_1.rev3(lists.my_list500)"
# 1000 loops, best of 5: 48.6 usec per loop
# "les_4_task_1.rev3(lists.my_list1000)"
# 1000 loops, best of 5: 92.2 usec per loop
# *********************************************



# ************************************************* Вывод **************************************************************
# Получились достаточно интересные результаты при замерах времени работы данных трех алгоритмов на заранее
# сгенерированных списках. Алгоритм под номером один работает по принципу обхода списка циклом, эмпирическая
# сложность такого алгоритма O(n). Данный алгоритм показал себя хуже всех по времени работы на маленьких списках,
# но лучше всех остальных по времени работы на больших списках.
# Алгоритм под номером два работает по принципу сортировки, эмпирическая сложность такого алгоритма O(nlog(n)).
# Данный алгоритм по времени работы на маленьких саисках показал себя лучше всех. А на списках длины 10000, time it
# выдал достаточно интересное сообщение о ненадежности результатов и якобы его время работы хуже остальных (4.59 с).
# Третий алгоритм работает по принципу нахождения min и max в списке при помощи встроенных функций, эмпирическая
# сложность такого алгоритма равна O(n). Данный алгоритм показал время работы примерно такое же как и первый на
# небольших списках. На больших списках они вели себя с первым примерно одинаково.
# Вывод можно сделать следующий: в рамках данной задачи, для небольших списков (до 1000 эл.) - стоит выбирать
# алгоритм 2. Если списки больше - стоит выбирать между 1 и 3 алгоритмом.