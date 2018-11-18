# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random

array = [random.randint(-100, 99) for i in range(10)]
array_1 = array[:]

def bubble_sort(array, order = 0):
    '''Сортировка методом пузырька

     Аргументы:
     array -- массив для сортировки
     order -- порядок сортировки, 0 - по возрастанию, 1 - по убыванию (default = 0)
     '''
    n = 1
    if order == 0:
        while n < len(array):
            for i in range(len(array) - n):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            n += 1
    elif order == 1:
        while n < len(array):
            for i in range(len(array) - n):
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            n += 1

    return array

bubble_sort(array, 1)

print(f'Исходный массив: {array_1}')
print(f'Отсортированный массив: {array}')