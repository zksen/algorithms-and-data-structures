# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
import collections

companies = collections.defaultdict()
higher = collections.deque()
below = collections.deque()
all_profit = 0
NUMB_QUARTERS = 4

while True:
    try:
        n = int(input('Введите количество компаний: '))
    except ValueError:
        print('Недопустимое значение. Введите целое положительное число!')
        continue
    break

for i in range(n):
    name = input(f'\nВведите название {i + 1}й компании: ')
    profit = 0
    q = 1
    while q <= NUMB_QUARTERS:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Недопустимое значение!')
            continue
        q += 1
    companies[name] = profit
    all_profit += profit

mid_profit = all_profit / n
for i, item in companies.items():
    if item >= mid_profit:
        higher.append(i)
    else:
        below.append(i)
print(f'Средняя прибыль для всех компаний составила: {mid_profit}')
print(f'Прибыль выше среднего у {len(higher)} компаний:')
for name in higher:
    print(name)
print(f'Прибыль ниже среднего у {len(below)} компаний:')
for name in below:
    print(name)
