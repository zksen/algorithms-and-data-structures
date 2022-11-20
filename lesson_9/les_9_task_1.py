# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
# считается не решённой.
def my_func(value):
    length = len(value)
    l1 = []
    letter = 26

    for i in range(length):
        for j in range(i, length + 1):
            if i != j:
                l1.append(sum([(ord(char) - ord('a') + 1) * letter ** eq for eq, char in enumerate(value[i:j])]))
    return len(set(l1)) - 1


print(my_func('aaa'))