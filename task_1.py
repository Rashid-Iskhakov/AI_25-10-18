# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трехзначное число: '))

a1 = a // 100
a2 = (a % 100) // 10
a3 = a % 10

summa = a1 + a2 + a3
mult = a1 * a2 * a3

# print(f'Сумма цифр трехзначного числа = {summa}')
# print(f'Произведение цифр трехзначного числа = {mult}')

import func_support

# Вариант 1
total_size = func_support.count_size(a)
total_size += func_support.count_size(a1)
total_size += func_support.count_size(a2)
total_size += func_support.count_size(a3)
total_size += func_support.count_size(summa)
total_size += func_support.count_size(mult)
print(f'В программе было задействовано {total_size} байт информации')

# Вариант 2
# Не уверен, что через eval корректно делать, но переменные удалось получить только в качестве строк
var_lst = [i for i in func_support.get_vars(locals()) if i != 'func_support' and i != 'total_size']

total_size_1 = 0

for vars in var_lst:
    total_size_1 += func_support.count_size(eval(vars))\

print(f'В программе было задействовано {total_size_1} байт информации')
print(total_size == total_size_1)
