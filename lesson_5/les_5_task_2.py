# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа.
from collections import defaultdict
from collections import deque

signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1
print(table)


def ddex(str):
    dex = 0
    num = deque(str)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def hhex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


num_1 = ddex(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
num_2 = ddex(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {hhex(num_1 + num_2)}')
print(f'Произведение чисел: {hhex(num_1 * num_2)}')