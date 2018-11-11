# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

# умножение не реализовано :(

from collections import deque
from collections import defaultdict

a = deque(input('Число a = '))
b = deque(input('Число b = '))

max_len = max(len(a), len(b))

if len(a) < max_len:
    for i in range(max_len - len(a)):
        a.appendleft(0)
elif len(b) < max_len:
    for i in range(max_len - len(b)):
        b.appendleft(0)

a.reverse()
b.reverse()

def sum_16(a, b, add_num):
    a = str(a).upper()
    b = str(b).upper()

    num16 = '0123456789ABCDEF'
    calc_deque = deque(num16, maxlen=16)

    support_deque = deque()

    for i in range(len(num16)):
        support_deque.append(i)

    calc_dict = defaultdict(int)
    for idx, value in enumerate(num16):
        calc_dict[value] = idx

    a_dict = calc_dict[a]
    b_dict = calc_dict[b]

    if add_num:
        calc_deque.rotate(-a_dict - 1)
    else:
        calc_deque.rotate(-a_dict)

    result = calc_deque[b_dict]

    if b_dict >= len(calc_deque) - a_dict - 1:
        result_add = True
    else:
        result_add = False

    result_lst = [result, result_add]

    return result_lst

# aaw = sum_16('3', 'f', False)
# print(aaw)

add_num = False
result = deque()

for idx in range(max_len):
    result_sup = sum_16(a[idx], b[idx], add_num)
    add_num = result_sup[1]
    result.appendleft(result_sup[0])

if add_num:
    result.appendleft(1)

print(result)





