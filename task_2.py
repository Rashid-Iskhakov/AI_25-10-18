# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

array = [round(random.random() * 50, 3) for i in range(10)]
random.shuffle(array)
array_1 = array[:]

def merge_sort(array):
    if len(array) > 1:
        n = len(array) // 2
        array1 = array[:n]
        array2 = array[n:]

        merge_sort(array1)
        merge_sort(array2)

        i, j, k = 0, 0, 0
        while j < len(array2) and i < len(array1):
            if array2[j] <= array1[i]:
                array[k] = array2[j]
                j += 1
            else:
                array[k] = array1[i]
                i += 1
            k += 1

        while j < len(array2):
            array[k] = array2[j]
            j += 1
            k += 1

        while i < len(array1):
            array[k] = array1[i]
            i += 1
            k += 1

merge_sort(array)

print(f'Исходный массив: {array_1}')
print(f'Отсортированный массив: {array}')



