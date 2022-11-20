"""4. Определить, какое число в массиве встречается чаще всего."""
import random
size = 30
my_list = [random.randint(0, 10) for el in range(size)]

my_list2 = [(x, len([eq for eq in my_list if eq == x])) for x in set(my_list)]
spam = my_list2[0][1]
for i in range(len(my_list2)):
    if spam <= my_list2[i][1]:
        spam = my_list2[i][1]
my_list3 = [eq[0] for eq in my_list2 if eq[1] == spam]
print(my_list)
print('Чаще всего встречаются числа: ')
for item in my_list3:
    print(item)