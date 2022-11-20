import random as rnd

my_file = open("lists2.py", "w", encoding="utf-8")

lists = [[rnd.randint(1, 100000) for _ in range(1, 10000)] for el in range(1, 1000)]

my_file.write(f'\nmy_list = {lists}')