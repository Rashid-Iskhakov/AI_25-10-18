# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

array = [random.randint(0, 100) for i in range(10)]
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

array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)