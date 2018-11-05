# Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(0, 10) for i in range(10)]
print(array)

frequency = 0
cur_frequency = 0
num = None

for i in array:
    cur_frequency = array.count(i)

    if cur_frequency > frequency:
        frequency = cur_frequency
        num = i

print(f'Число {num} встречается в массиве чаще всего. Количество повторений: {frequency}')