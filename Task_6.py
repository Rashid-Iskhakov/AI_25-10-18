# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем
# за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное
# пользователем число. Если за 10 попыток число не отгадано, то вывести его.

import random

random_num = random.randint(0, 100)
need_answer = True

for i in range(10):
    answer = int(input('Введите число: '))

    if random_num < answer:
        print('Загаданное число меньше')
    elif random_num > answer:
        print('Загаданное число больше')
    else:
        print('Вы угадали!')
        need_answer = False
        break



if need_answer == True:
    print(f'Загаданное число: {random_num}')