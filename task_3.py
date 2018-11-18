# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше ее.

import random
SIZE = 100

m = int(input('Будет сгенирован массив размером 2m + 1, введите m: '))

array = [random.randint(1, SIZE) for i in range(2 * m + 1)]
array_1 = array[:]

def find_median(array):

    for i in range(len(array) // 2):
        array.remove(min(array))

    x = min(array)

    return x

array_med = find_median(array)

print(f'Исходный массив: {array_1}')
print(f'Медиана: {array_med}')
