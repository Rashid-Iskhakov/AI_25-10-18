# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли

from collections import defaultdict

lst_ent = []
lst_rev = []

ent_num = int(input('Введите количество предприятий: '))

for j in range(ent_num):
    ent_name = input('Введите название предприятия: ')

    lst_ent.append(ent_name)

    rev = 0

    for i in range(4):
        rev += float(input(f'Введите прибыль за {i+1} квартал: '))

    lst_rev.append(rev)

    ent_dict = defaultdict(float)

    for idx, ent in enumerate(lst_ent):
        ent_dict[ent] += lst_rev[idx]

print(ent_dict)

sum_rev = 0

for value in ent_dict.values():
        sum_rev += value

av_rev = sum_rev / len(ent_dict)

above_av = []
below_av = []


for key, value in ent_dict.items():
    if value > av_rev:
        above_av.append(key)
    elif value < av_rev:
        below_av.append(key)

print('Предприятия с выручкой выше среднего:')
for i in above_av:
    print(i, end='\n')

print()
print('Предприятия с выручкой ниже среднего:')
for i in below_av:
    print(i, end='\n')



# print(enterprise)


# lst = [('Apple', 1, 3, 4, 5)]
# c = defaultdict(list)
# for key, value in lst:
#     c[key].append(value)
#
# print(c)

# while True:
