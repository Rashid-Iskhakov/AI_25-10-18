import math
import cProfile

def test_prime_num(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    for idx, item in enumerate(lst, 1):
        assert item == func(idx)
        print(f'Test {idx}: OK')

def prime_num_erat(n):

    res = []
    n_sieve = int(6.1184 * n)

    # y = 6.1184 * n - 63.869 - линейная регрессия, где n - порядковый номер простого
    # числа, y - простое число. -63.869 для упрощения отбрасываем

    while len(res) < n:
        n_sieve += 100

        sieve = [i for i in range(n_sieve)]
        sieve[1] = 0

        for i in range(2, n_sieve):
            if sieve[i] != 0:
                j = i + i
                while j < n_sieve:
                    sieve[j] = 0
                    j += i

        res = [i for i in sieve if i != 0]

    return res[n - 1]

def prime_num(n):

    res = []
    n_sieve = int(6.1184 * n)

    while len(res) < n:
        n_sieve += 100

        sieve = [i for i in range(n_sieve)]
        sieve[1] = 0

        for i in range(3, n_sieve):
            if sieve[i] != 0:

                j = 2

                while j <= math.sqrt(i): # наименьший делитель составного числа i не превосходит sqrt(i)
                    if sieve[i] % j == 0:
                        sieve[i] = 0
                    j += 1


        res = [i for i in sieve if i != 0]

    return res[n - 1]


# "task_2.prime_num(10)"
# 100 loops, best of 3: 871 usec per loop
# "task_2.prime_num(20)"
# 100 loops, best of 3: 1.39 msec per loop
# "task_2.prime_num(30)"
# 100 loops, best of 3: 2.02 msec per loop

# cProfile.run('prime_num(10)')  1280    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
# cProfile.run('prime_num(20)')  2091    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
# cProfile.run('prime_num(30)')  3030    0.001    0.000    0.001    0.000 {built-in method math.sqrt}


# "task_2.prime_num_erat(10)"
# 100 loops, best of 3: 106 usec per loop
# "task_2.prime_num_erat(20)"
# 100 loops, best of 3: 146 usec per loop
# "task_2.prime_num_erat(30)"
# 100 loops, best of 3: 181 usec per loop

# cProfile для prog_num_erat дает одинаковые результаты

# Вывод Решето Эратосфена более эффективный метод по сравнению с простым перебором



# test_prime_num(prime_num)
# print()
# test_prime_num(prime_num_erat)



