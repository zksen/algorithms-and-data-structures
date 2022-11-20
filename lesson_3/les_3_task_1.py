"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
 Примечание: 8 разных ответов."""

# 8 обходов
my_2 = len([el for el in range(2, 100) if el % 2 == 0])
my_3 = len([el for el in range(2, 100) if el % 3 == 0])
my_4 = len([el for el in range(2, 100) if el % 4 == 0])
my_5 = len([el for el in range(2, 100) if el % 5 == 0])
my_6 = len([el for el in range(2, 100) if el % 6 == 0])
my_7 = len([el for el in range(2, 100) if el % 7 == 0])
my_8 = len([el for el in range(2, 100) if el % 8 == 0])
my_9 = len([el for el in range(2, 100) if el % 9 == 0])
print(f'{my_2}\n{my_3}\n{my_4}\n{my_5}\n{my_6}\n{my_7}\n{my_8}\n{my_9}')

print('*' * 30)

# 1 обход
my_list = [[eq, 0] for eq in range(2, 10)]
for el in range(2, 100):
    for i in range(len(my_list)):
        if el % my_list[i][0] == 0:
            my_list[i][1] += 1

for item in my_list:
    print(item[1])
