"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
import random
size1 = 4
size2 = 4
my_matrix = [[random.randint(1, 10) for _ in range(size1)] for _ in range(size2)]
for line in my_matrix:
    for i in line:
        print(f'{i:>4}', end='')
    print('')

mx = -1
for j in range(size1):
    mn = 10
    for i in range(size2):
        if my_matrix[i][j] < mn:
            mn = my_matrix[i][j]
    if mn > mx:
        mx = mn


print(f'Максимальный среди минимальных по столбцам: {mx}')