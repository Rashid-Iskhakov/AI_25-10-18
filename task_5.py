# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
SIZE = 10

array = [random.randint(- SIZE, SIZE) for i in range(10)]
print(array)
max_negative = - SIZE - 1

for i in array:
    if i < 0 and i > max_negative:
        max_negative = i

print(f'Максимальный отрицательный элемент: {max_negative}' if max_negative != (- SIZE - 1) else \
        'Отрицательные элементы отсутствуют')
