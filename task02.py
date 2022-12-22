# Задача 2:
# Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

from msilib import sequence

n = int(input('Введите число: '))

def get_squerence(n):
    return[round((1 + 1/x)**x, 5) for x in range(1, n + 1)]

num = get_squerence(n)
print(num)
print(round(sum(num), 5))