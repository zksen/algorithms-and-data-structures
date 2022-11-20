"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр."""
NUMB = int(input('Введите сколько чисел: '))
maxis = 0
result = 0
while NUMB > 0:
    number = int(input())
    NUMB -= 1
    i = 1
    summa = 0
    my_number = number
    while i <= len(str(my_number)):
        summa += my_number % 10
        my_number //= 10
        i += 1
    if summa >= maxis:
        maxis = summa
        result = number
print(result)
