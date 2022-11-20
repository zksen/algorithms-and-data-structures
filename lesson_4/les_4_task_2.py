import cProfile


def alg1(n):
    """Первый алгоритм O(n^2)"""

    lst = []
    k = 0
    for i in range(2, n + 1):
        for j in lst:
            if i % j == 0:
                k += 1
                break
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst[len(lst) - 1]


# "les_4_task_2.alg1(10)"
# 1000 loops, best of 5: 2.47 usec per loop

# "les_4_task_2.alg1(20)"
# 1000 loops, best of 5: 5.42 usec per loop

# "les_4_task_2.alg1(100)"
# 1000 loops, best of 5: 36.1 usec per loop

# "les_4_task_2.alg1(500)"
# 1000 loops, best of 5: 353 usec per loop

# "les_4_task_2.alg1(1000)"
# 1000 loops, best of 5: 1.04 msec per loop

# "les_4_task_2.alg1(2000)"
# 1000 loops, best of 5: 5.35 msec per loop

# "les_4_task_2.alg1(5000)"
# 1000 loops, best of 5: 26.5 msec per loop

def alg2(n):
    """Второй алгоритм O(nlog(log(n)))"""

    lst = list(range(n + 1))
    lst[1] = 0
    for i in lst:
        if i > 1:
            for j in range(2*i, len(lst), i):
                lst[j] = 0
    lst1 = [x for x in lst if x != 0]
    return lst1[len(lst1) - 1]



# "les_4_task_2.alg2(10)"
# 1000 loops, best of 5: 3.48 usec per loop

# "les_4_task_2.alg2(20)"
# 1000 loops, best of 5: 5.96 usec per loop

# "les_4_task_2.alg2(100)"
# 1000 loops, best of 5: 24.8 usec per loop

# "les_4_task_2.alg2(500)"
# 1000 loops, best of 5: 121 usec per loop

# "les_4_task_2.alg2(1000)"
# 1000 loops, best of 5: 244 usec per loop

# "les_4_task_2.alg2(2000)"
# 1000 loops, best of 5: 830 usec per loop

# "les_4_task_2.alg2(5000)"
# 1000 loops, best of 5: 2.21 msec per loop



# ************************************************* Вывод **************************************************************
# Первый алгоритм имеет эмпирическую сложность O(n^2). По времени работы алгоритма также видно, что работает он
# достаточно медленно на большом n начиная с 1000. Второй алгоритм (решето Эратосфена) имеет эмпирическую сложность
# O(nlog(log(n))) и работает быстрее первого. Он делает меньше проверок внутри внутреннего цикла, засчет этого
# и происходит выигрыш по времени.