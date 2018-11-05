# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [random.randint(0, 100) for i in range(10)]
#array = [1, 1, 1, 1, 1]
print(array)

array_min = array_max = array[0]
j = min_index = max_index = 0

for i in array:
    if i < array_min:
        array_min = i
        min_index = j

    if i > array_max:
        array_max = i
        max_index = j

    j += 1
print(f'max: {array_max}')
print(f'min: {array_min}')

summa = 0

if min_index < max_index:
    for i in range(min_index + 1, max_index):
        summa += array[i]
else:
    for i in range(max_index + 1, min_index):
        summa += array[i]

print(summa)