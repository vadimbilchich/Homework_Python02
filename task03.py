# Задача 3:
# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random
lst = [random.randint(0, 10) for i in range(random.randint(5, 20))]
print(f'Исходный список: \n{lst}')
random.shuffle(lst)
print(f'Список после перемешивания: \n{lst}')