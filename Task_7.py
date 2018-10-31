# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число.

n = int(input('Введите любое натуральное число: '))

num_1 = n * (n + 1) / 2
num_2 = 0

for i in range(n):
    num_2 = num_2 + (i + 1)

print(f'число 1: {num_1}, число 2: {num_2}')

if num_1 == num_2:
    print('Числа равны!')
