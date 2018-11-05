# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

array = [random.randint(0, 10) for i in range(10)]
print(array)

array_min1 = array_min2 = array[0]

for i in array:
    if i <= array_min1:
        array_min2 = array_min1
        array_min1 = i
    elif i > array_min1 and i < array_min2:
        array_min2 = i

print(f'Минимальные числа в массиве: {array_min1}, {array_min2}')

