# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо
# заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

array_1 = [random.randint(0, 100) for i in range(10)]
array_2 = [i for i in range(len(array_1)) if array_1[i] % 2 == 0]

# print(array_1)
# print(array_2)

import func_support

# Вариант 1

total_size = func_support.count_size(array_1)
total_size += func_support.count_size(array_2)
print(f'В программе было задействовано {total_size} байт информации')

# Вариант 2
# Не уверен, что через eval корректно делать, но переменные удалось получить только в качестве строк

var_lst = [i for i in func_support.get_vars(locals()) if i != 'func_support' and i != 'total_size' \
           and i != 'random']

total_size_1 = 0

for vars in var_lst:
    total_size_1 += func_support.count_size(eval(vars))

print(f'В программе было задействовано {total_size_1} байт информации')
print(total_size == total_size_1)