# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

import cProfile

def test_prog(func):
    lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875, 0.6640625]
    for idx, item in enumerate(lst, 1):
        assert item == func(idx)
        print(f'Test {idx}: OK')

# вариант 1. Реализован в ДЗ-2
def prog_sum(n):
    x = 1
    sum_x = x

    for i in range(n-1):
        x *= (-0.5)
        sum_x += x

    return sum_x

# вариант 2. Рекурсия
def prog_sum_rec(n):

    def prog_rec(n):
        if n < 2:
            return 1
        return prog_rec(n - 1) * (-0.5)

    if n < 2:
        return 1
    return prog_sum_rec(n - 1) + prog_rec(n)


# "task_1.prog_sum(10)"
# 100 loops, best of 3: 2.35 usec per loop
# "task_1.prog_sum(15)"
# 100 loops, best of 3: 3.1 usec per loop
# "task_1.prog_sum(20)"
# 100 loops, best of 3: 3.84 usec per loop
# "task_1.prog_sum(30)"
# 100 loops, best of 3: 5.38 usec per loop

# cProfile для prog_sum дает одинаковые результаты

# "task_1.prog_sum_rec(10)"
# 100 loops, best of 3: 23 usec per loop
# "task_1.prog_sum_rec(15)"
# 100 loops, best of 3: 46.8 usec per loop
# "task_1.prog_sum_rec(20)"
# 100 loops, best of 3: 81.7 usec per loop
# "task_1.prog_sum_rec(30)"
# 100 loops, best of 3: 168 usec per loop

# cProfile.run('prog_sum_rec(10)')
# 10/1    0.000    0.000    0.000    0.000 task_1.py:22(prog_sum_rec)
# 54/9    0.000    0.000    0.000    0.000 task_1.py:24(prog_rec)
# cProfile.run('prog_sum_rec(15)')
# 15/1    0.000    0.000    0.000    0.000 task_1.py:22(prog_sum_rec)
# 119/14    0.000    0.000    0.000    0.000 task_1.py:24(prog_rec)
# cProfile.run('prog_sum_rec(20)')
# 20/1    0.000    0.000    0.000    0.000 task_1.py:22(prog_sum_rec)
# 209/19    0.000    0.000    0.000    0.000 task_1.py:24(prog_rec)
# cProfile.run('prog_sum_rec(30)')
# 30/1    0.000    0.000    0.000    0.000 task_1.py:22(prog_sum_rec)
# 464/29    0.000    0.000    0.000    0.000 task_1.py:24(prog_rec)

# Вывод: Алгоритм реализованный в ДЗ имеет меньшую асимптотику. Зависимость близка к линейной.
# Рекурсивный алгоритм имеет близкую к квадратичной зависимость скорости выполнения.

# test_prog(prog_sum)
# print()
# test_prog(prog_sum_rec)

