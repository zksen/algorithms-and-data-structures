"""Определить, является ли год, который ввел пользователь, високосным или не високосным."""
y = int(input("Введите год: "))
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print(f"Год {y} високосный")
else:
    print(f"Год {y} невисокосный")